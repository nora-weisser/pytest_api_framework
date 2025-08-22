from utils import api_util
from utils.api_util import build_url
from TestData.endpoints import LOGIN_PATH
from utils.assertions import assert_status_code
from utils.schema_validator import response_schema_validator
from TestData.schemas.login import LoginResponse
from TestData.expected_responses import invalid_credentials_response
import pytest


@pytest.mark.parametrize(
    "username, password, expected_status",
    [
        ("admin", "password", 200),
        ("admin", "wrongpassword", 401),
        ("unknown", "password", 401),
        ("", "", 401),
    ]
)
def test_login(username, password, expected_status):
    url = build_url(LOGIN_PATH)
    login_data = {
        "username": username,
        "password": password
    }
    response = api_util.post_api(url, login_data)

    if expected_status == 200:
        response_schema_validator(LoginResponse, response.json())
    else:
        assert response.json() == invalid_credentials_response

    assert_status_code(response, expected_status)
