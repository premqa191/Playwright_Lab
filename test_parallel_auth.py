from playwright.sync_api import expect


def test_secure_area_heading_and_logout(auth_page):
    auth_page.goto("https://the-internet.herokuapp.com/secure")
    expect(auth_page.get_by_role("heading", name="Secure Area", exact=True)).to_be_visible()
    expect(auth_page.get_by_role("link", name="Logout")).to_be_visible()


def test_secure_area_welcome_banner(auth_page):
    auth_page.goto("https://the-internet.herokuapp.com/secure")
    expect(auth_page.locator("h4.subheader")).to_contain_text("Welcome to the Secure Area.")
