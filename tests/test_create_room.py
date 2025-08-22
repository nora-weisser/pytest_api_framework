from utils import api_util
from utils.assertions import assert_status_code
from TestData.expected_responses import success_response, authentication_required_response

def test_create_new_room_returns_200(auth_headers, room_url, new_room_data):
    response = api_util.post_api(room_url, new_room_data, auth_headers)
    assert_status_code(response, 200)
    assert response.json() == success_response


def test_create_new_room_without_authentication_returns_401(room_url, new_room_data):
    response = api_util.post_api(room_url, new_room_data)
    assert_status_code(response, 401)
    assert response.json() == authentication_required_response