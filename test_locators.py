import pytest
from playwright.sync_api import sync_playwright

def test_user_login_flow():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://the-internet.herokuapp.com/login')
        page.get_by_label('Username').fill('tomsmith')
        page.get_by_label('Password').fill('SuperSecretPassword!')
        page.get_by_role('button', name='Login').click()
        flash_message = page.locator('#flash')
        assert 'You logged into a secure area!' in flash_message.text_content()
        browser.close()
