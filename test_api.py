import pytest
from playwright.sync_api import sync_playwright

def test_get_api_request():
    with sync_playwright() as p:
        # API కాంటెక్స్ట్ సృష్టించడం
        api_request_context = p.request.new_context(base_url="https://catfact.ninja")
        response = api_request_context.get('/fact')
        
        assert response.ok
        data = response.json()
        assert 'fact' in data
        print(f'\nAPI Response Fact: {data["fact"]}')
        
        api_request_context.dispose()
