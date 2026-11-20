import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

AUTH_FILE = Path("reports/auth.json")
SCREENSHOT_FILE = Path("reports/hybrid_check.png")


def test_api_login_and_ui_hybrid():
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        # 1. APIRequestContext ద్వారా బ్యాకెండ్ API కాల్ (బ్రౌజర్ UI తెరవకుండా)
        api_ctx = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            extra_http_headers={"Accept": "application/json"},
        )
        api_response = api_ctx.post(
            "/posts",
            data={
                "title": "hybrid-session-setup",
                "body": "pre-seed-test-data",
                "userId": 1,
            },
        )
        assert api_response.ok, f"API setup failed: {api_response.status}"
        created_record = api_response.json()
        assert created_record.get("id") is not None
        api_ctx.dispose()

        # 2. UI కాంటెక్స్ట్ సృష్టించి, సెషన్/స్టోరేజ్ స్టేట్‌ను auth.json లో సేవ్ చేయడం
        browser = p.chromium.launch(headless=True)
        setup_context = browser.new_context()
        setup_page = setup_context.new_page()
        setup_page.goto("https://the-internet.herokuapp.com/login")
        setup_page.evaluate(
            "([seedId]) => window.localStorage.setItem('hybrid_api_seed_id', seedId)",
            [str(created_record["id"])],
        )
        setup_context.storage_state(path=str(AUTH_FILE))
        setup_context.close()

        # 3. సేవ్ చేసిన storage_state (auth.json) తో కొత్త UI కాంటెక్స్ట్ తెరవడం
        hybrid_context = browser.new_context(storage_state=str(AUTH_FILE))
        hybrid_page = hybrid_context.new_page()
        hybrid_page.goto("https://the-internet.herokuapp.com/login")

        expect(hybrid_page.get_by_role("heading", name="Login Page")).to_be_visible()
        stored_val = hybrid_page.evaluate(
            "() => window.localStorage.getItem('hybrid_api_seed_id')"
        )
        assert stored_val == str(created_record["id"])

        hybrid_page.screenshot(path=str(SCREENSHOT_FILE))
        hybrid_context.close()
        browser.close()

    # 4. హోస్ట్‌లో ఫైల్స్ సేవ్ అయ్యాయా లేదా అని నిర్ధారించడం
    assert AUTH_FILE.exists(), "reports/auth.json was not created"
    assert SCREENSHOT_FILE.exists(), "reports/hybrid_check.png was not created"
    parsed_state = json.loads(AUTH_FILE.read_text(encoding="utf-8"))
    assert "origins" in parsed_state
