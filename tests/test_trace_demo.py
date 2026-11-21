import os
from playwright.sync_api import sync_playwright
from pages.secure_page import SecurePage


def test_secure_page_with_trace():
    auth_file = "reports/auth_state.json"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            storage_state=auth_file if os.path.exists(auth_file) else None
        )
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = context.new_page()
        if not os.path.exists(auth_file):
            page.goto("https://the-internet.herokuapp.com/login")
            page.get_by_label("Username").fill("tomsmith")
            page.get_by_label("Password").fill("SuperSecretPassword!")
            page.get_by_role("button", name="Login").click()

        SecurePage(page).open().verify_loaded()

        context.tracing.stop(path="reports/trace.zip")
        browser.close()
