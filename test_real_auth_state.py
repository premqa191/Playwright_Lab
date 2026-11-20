import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

AUTH_STATE_FILE = Path("reports/auth_state.json")


def test_real_login_and_reuse_session():
    AUTH_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        # 1. ఒకసారి UI ద్వారా లాగిన్ చేసి storage_state (auth_state.json) సేవ్ చేయడం
        login_context = browser.new_context()
        login_page = login_context.new_page()

        login_page.goto("https://the-internet.herokuapp.com/login")
        login_page.get_by_label("Username").fill("tomsmith")
        login_page.get_by_label("Password").fill("SuperSecretPassword!")
        login_page.get_by_role("button", name="Login").click()

        expect(login_page.locator("#flash")).to_contain_text("You logged into a secure area!")

        login_context.storage_state(path=str(AUTH_STATE_FILE))
        login_context.close()

        # 2. సేవ్ చేసిన auth_state.json తో కొత్త కాంటెక్స్ట్ తెరవడం (మళ్ళీ లాగిన్ ఫారమ్ నింపకుండా)
        reused_context = browser.new_context(storage_state=str(AUTH_STATE_FILE))
        reused_page = reused_context.new_page()

        reused_page.goto("https://the-internet.herokuapp.com/secure")
        expect(reused_page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
        expect(reused_page.get_by_role("link", name="Logout")).to_be_visible()

        reused_page.screenshot(path="reports/secure_area_reused.png")
        reused_context.close()
        browser.close()

    assert AUTH_STATE_FILE.exists(), "reports/auth_state.json was not created"
    state_data = json.loads(AUTH_STATE_FILE.read_text(encoding="utf-8"))
    assert "cookies" in state_data and "origins" in state_data
