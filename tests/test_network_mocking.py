import json
from playwright.sync_api import expect, sync_playwright


def test_mock_api_response_in_page():
    mock_payload = {
        "userId": 99,
        "id": 999,
        "title": "Mocked Title From Playwright Route",
        "body": "Intercepted cleanly without hitting live backend.",
    }

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        def handle_route(route):
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps(mock_payload),
            )

        page.route("**/posts/1", handle_route)

        page.set_content("""
            <html>
              <body>
                <h1 id="title">Loading...</h1>
                <script>
                  fetch("https://jsonplaceholder.typicode.com/posts/1")
                    .then((res) => res.json())
                    .then((data) => {
                      document.getElementById("title").textContent = data.title;
                    });
                </script>
              </body>
            </html>
        """)

        expect(page.locator("#title")).to_have_text("Mocked Title From Playwright Route")
        browser.close()


def test_mock_network_failure_shows_fallback_message():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.route("**/posts/1", lambda route: route.abort("failed"))

        page.set_content("""
            <html>
              <body>
                <h1 id="title">Loading...</h1>
                <script>
                  fetch("https://jsonplaceholder.typicode.com/posts/1")
                    .then((res) => res.json())
                    .then((data) => {
                      document.getElementById("title").textContent = data.title;
                    })
                    .catch(() => {
                      document.getElementById("title").textContent = "Service Unavailable";
                    });
                </script>
              </body>
            </html>
        """)

        expect(page.locator("#title")).to_have_text("Service Unavailable")
        browser.close()
