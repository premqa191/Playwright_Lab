import pytest
from playwright.sync_api import sync_playwright

def test_web_interactions():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Checkboxes Interaction
        page.goto('https://the-internet.herokuapp.com/checkboxes')
        checkbox1 = page.locator('input[type="checkbox"]').first
        checkbox1.check()
        assert checkbox1.is_checked()

        # 2. Dropdown Interaction
        page.goto('https://the-internet.herokuapp.com/dropdown')
        dropdown = page.locator('#dropdown')
        dropdown.select_option(value='2')
        assert dropdown.input_value() == '2'

        # 3. JavaScript Alert Handling
        page.goto('https://the-internet.herokuapp.com/javascript_alerts')
        page.on('dialog', lambda dialog: dialog.accept())
        page.get_by_role('button', name='Click for JS Alert').click()
        result_text = page.locator('#result').text_content()
        assert 'You successfully clicked an alert' in result_text

        browser.close()
