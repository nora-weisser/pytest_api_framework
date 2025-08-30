from utils.assertions import assert_status_code
from utils.schema_validator import response_schema_validator
from test_data.schemas.login_response import LoginResponse
from test_data.expected_responses import invalid_credentials_response
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
def test_login(auth_api, username, password, expected_status):
    response = auth_api.authenticate(username, password)

    if expected_status == 200:
        response_schema_validator(LoginResponse, response.json())
    else:
        assert response.json() == invalid_credentials_response

    assert_status_code(response, expected_status)
