import allure
import requests, json
from urllib.parse import urljoin
from utils.myconfigparser import getURL

class APIClient:
    def __init__(self):
        self.base_url = getURL()
        self.default_headers = {
            'Content-Type': 'application/json'
        }

    def build_url(self, path: str) -> str:
        return urljoin(self.base_url, path)

    @allure.step('Performing GET API Request')
    def get(self, path: str, add_headers: dict = None):
        url = self.build_url(path)
        headers = self.default_headers.copy()
        if isinstance(add_headers, dict):
            headers.update(add_headers)
        response = requests.get(url, verify=False, headers=headers)
        print(f"\nRequest URL: {url}")
        print(f"\nRequest Headers: {response.request.headers}")
        print(f"\nResponse: {json.dumps(response.json(), indent=3)}")
        return response

    @allure.step('Performing POST API Request')
    def post(self, path: str, body: dict, add_headers: dict = None):
        url = self.build_url(path)
        headers = self.default_headers.copy()
        if isinstance(add_headers, dict):
            headers.update(add_headers)
        response = requests.post(url, json=body, headers=headers, verify=False)
        print(f"\nRequest URL: {url}")
        print(f"\nRequest Body: {json.dumps(body, indent=3)}")
        print(f"\nRequest Headers: {response.request.headers}")
        print(f"\nResponse: {json.dumps(response.json(), indent=3)}")
        return response