from playwright.sync_api import expect


def test_seeded_record_and_ui_flow_a(auth_page, seeded_post):
    assert seeded_post["title"].startswith("Playwright-Lab-Seed-")
    assert seeded_post["id"] is not None

    auth_page.goto("https://the-internet.herokuapp.com/secure")
    expect(auth_page.get_by_role("heading", name="Secure Area", level=2, exact=True)).to_be_visible()


def test_seeded_record_and_ui_flow_b(auth_page, seeded_post):
    assert seeded_post["title"].startswith("Playwright-Lab-Seed-")
    assert seeded_post["id"] is not None

    auth_page.goto("https://the-internet.herokuapp.com/checkboxes")
    expect(auth_page.get_by_role("heading", name="Checkboxes", level=3)).to_be_visible()