import requests
from urllib.parse import urljoin
from utils.myconfigparser import getURL

BASE_URL = getURL()

def build_url(path: str) -> str:
    return urljoin(BASE_URL, path)

def getAPI(url: str):
    response = requests.get(url)
    return response