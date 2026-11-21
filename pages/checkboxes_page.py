from playwright.sync_api import expect


class CheckboxesPage:
    URL = "https://the-internet.herokuapp.com/checkboxes"

    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Checkboxes", level=3)
        self.checkboxes = page.locator("#checkboxes input[type='checkbox']")

    def open(self):
        self.page.goto(self.URL)
        return self

    def verify_loaded(self):
        expect(self.heading).to_be_visible()
        expect(self.checkboxes).to_have_count(2)
        return self

    def toggle_first_checkbox(self):
        first = self.checkboxes.nth(0)
        if first.is_checked():
            first.uncheck()
        else:
            first.check()
        return self
