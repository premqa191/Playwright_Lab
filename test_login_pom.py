import pytest
from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage

def test_valid_login_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        # Actions through Page Object
        login_page.navigate()
        login_page.login('tomsmith', 'SuperSecretPassword!')

        # Web-First Assertion
        expect(login_page.flash_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text('You logged into a secure area!')
        browser.close()

def test_invalid_login_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        login_page = LoginPage(page)

        # Invalid login flow
        login_page.navigate()
        login_page.login('invalid_user', 'wrong_pass')

        expect(login_page.flash_message).to_be_visible()
        expect(login_page.flash_message).to_contain_text('Your username is invalid!')
        browser.close()
