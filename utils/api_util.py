import requests, json
from urllib.parse import urljoin
from utils.myconfigparser import getURL

BASE_URL = getURL()

def build_url(path: str) -> str:
    return urljoin(BASE_URL, path)

def get_api(url: str, addHeaders=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | addHeaders) if isinstance(addHeaders, dict) else headers
    response = requests.get(url, verify=False, headers=headers)
    print("\nRequestURL: " + url)
    print("\nrequest headers: ", response.request.headers)
    print("\nresponse: ", json.dumps(response.json(), indent=3))
    return response

def post_api(url: str, body, addHeaders=None):
    headers = {'Content-Type': 'application/json'}
    headers = (headers | addHeaders) if isinstance(addHeaders, dict) else headers
    response = requests.post(url, json=body, headers=headers)
    print("\nRequestURL: " + url)
    print("\nrequest Data: ", body)
    print("\nrequest headers: ", response.request.headers)
    print("\nresponse: ", response.json())
    return response
