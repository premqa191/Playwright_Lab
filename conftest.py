import os
import uuid
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright, expect

AUTH_STATE_PATH = Path("reports/auth_state.json")


@pytest.fixture(scope="session")
def ensure_auth_state():
    AUTH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://the-internet.herokuapp.com/login")
        page.get_by_label("Username").fill("tomsmith")
        page.get_by_label("Password").fill("SuperSecretPassword!")
        page.get_by_role("button", name="Login").click()

        expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
        context.storage_state(path=str(AUTH_STATE_PATH))

        context.close()
        browser.close()
    return str(AUTH_STATE_PATH)


@pytest.fixture
def auth_page(ensure_auth_state):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=ensure_auth_state)
        page = context.new_page()
        yield page
        context.close()
        browser.close()

     
import json
import os
import uuid
from pathlib import Path
from urllib import request as url_request
import pytest
from playwright.sync_api import sync_playwright, expect

# ... (మీ పాత ensure_auth_state మరియు auth_page ఫిక్స్‌చర్లు అలాగే ఉంచండి) ...


class SimpleApiResponse:
    def __init__(self, status: int, body: str):
        self.status = status
        self.ok = 200 <= status < 300
        self._body = body

    def json(self):
        return json.loads(self._body) if self._body else {}


class SimpleApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def post(self, path: str, data: dict) -> SimpleApiResponse:
        url = f"{self.base_url}{path}"
        payload = json.dumps(data).encode("utf-8")
        req = url_request.Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with url_request.urlopen(req, timeout=15) as resp:
            return SimpleApiResponse(resp.status, resp.read().decode("utf-8"))

    def delete(self, path: str) -> SimpleApiResponse:
        url = f"{self.base_url}{path}"
        req = url_request.Request(url, method="DELETE")
        with url_request.urlopen(req, timeout=15) as resp:
            return SimpleApiResponse(resp.status, resp.read().decode("utf-8"))


@pytest.fixture(scope="session")
def api_base_url():
    return os.environ.get("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture
def api_client(api_base_url):
    return SimpleApiClient(api_base_url)


@pytest.fixture
def seeded_post(api_client):
    unique_title = f"Playwright-Lab-Seed-{uuid.uuid4().hex[:8]}"

    response = api_client.post(
        "/posts",
        data={
            "title": unique_title,
            "body": "Isolated test data seeded via API",
            "userId": 1,
        },
    )
    assert response.ok, f"Seed POST failed with status: {response.status}"
    created = response.json()

    yield {
        "id": created.get("id"),
        "title": unique_title,
    }

    post_id = created.get("id")
    if post_id is not None:
        cleanup_res = api_client.delete(f"/posts/{post_id}")
        print(f"\n[Cleanup] Removed post ID={post_id} (status={cleanup_res.status})")