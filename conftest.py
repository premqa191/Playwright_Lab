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
