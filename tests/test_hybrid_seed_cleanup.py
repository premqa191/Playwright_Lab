from pages.checkboxes_page import CheckboxesPage
from pages.secure_page import SecurePage


def test_seeded_record_and_ui_flow_a(auth_page, seeded_post):
    assert seeded_post["title"].startswith("Playwright-Lab-Seed-")
    assert seeded_post["id"] is not None

    SecurePage(auth_page).open().verify_loaded()


def test_seeded_record_and_ui_flow_b(auth_page, seeded_post):
    assert seeded_post["title"].startswith("Playwright-Lab-Seed-")
    assert seeded_post["id"] is not None

    CheckboxesPage(auth_page).open().verify_loaded().toggle_first_checkbox()
