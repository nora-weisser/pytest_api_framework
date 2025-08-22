import pytest
from TestData.endpoints import LOGIN_PATH
from utils.api_util import post_api
from utils.api_util import build_url
from TestData.endpoints import ROOM_PATH
from TestData.test_data.room_data import generate_room

# --- URLs ---
@pytest.fixture
def login_url():
    return build_url(LOGIN_PATH)

@pytest.fixture
def room_url():
    return build_url(ROOM_PATH)


# --- Data ---
@pytest.fixture
def new_room_data():
    return generate_room().model_dump(mode='json')

# --- Authentication ---
@pytest.fixture
def get_token(login_url):
    payload = {
          "username": "admin",
          "password": "password"
        }
    login_response = post_api(login_url, payload)
    response_body = login_response.json()
    token = response_body["token"]
    return token

@pytest.fixture
def auth_headers(get_token):
    return {'Cookie': f'token={get_token}'}
