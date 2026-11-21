import json
from urllib import error as url_error
from urllib import request as url_request


def _http_get(url: str):
    req = url_request.Request(url, method="GET")
    try:
        with url_request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body) if body else {}
    except url_error.HTTPError as exc:
        return exc.code, {}


def test_seeded_post_schema_and_types(seeded_post):
    assert isinstance(seeded_post["id"], int)
    assert seeded_post["id"] > 0
    assert seeded_post["title"].startswith("Playwright-Lab-Seed-")


def test_non_existent_post_returns_not_found(api_base_url):
    status, payload = _http_get(f"{api_base_url}/posts/999999")
    assert status == 404
    assert payload == {}
