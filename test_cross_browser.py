import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize('browser_name', ['chromium', 'firefox', 'webkit'])
def test_cross_browser_login(browser_name):
    with sync_playwright() as p:
        # ??????? ??????? ??????? ?? ????? ?????
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=True)
        page = browser.new_page()

        page.goto('https://the-internet.herokuapp.com/login')
        page.get_by_label('Username').fill('tomsmith')
        page.get_by_label('Password').fill('SuperSecretPassword!')
        page.get_by_role('button', name='Login').click()

        assert 'You logged into a secure area!' in page.locator('#flash').text_content()
        browser.close()
