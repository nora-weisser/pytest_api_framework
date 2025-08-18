import pytest
from utils import apiUtil
from TestData.endpoints import LOGIN_PATH
from utils.apiUtil import postAPI


@pytest.fixture
def get_token():
    login_url = apiUtil.build_url(LOGIN_PATH)
    payload = {
          "username": "admin",
          "password": "password"
        }
    login_response = postAPI(login_url, payload)
    response_body = login_response.json()
    token = response_body["token"]
    return token
