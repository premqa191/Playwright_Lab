from playwright.sync_api import expect


class SecurePage:
    URL = "https://the-internet.herokuapp.com/secure"

    def __init__(self, page):
        self.page = page
        self.heading = page.get_by_role("heading", name="Secure Area", level=2, exact=True)

    def open(self):
        self.page.goto(self.URL)
        return self

    def verify_loaded(self):
        expect(self.heading).to_be_visible()
