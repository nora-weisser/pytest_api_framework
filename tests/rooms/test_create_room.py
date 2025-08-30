import pytest
from test_data.test_data.room_data import generate_room
from utils.assertions import assert_status_code, assert_room_name_exists
from test_data.expected_responses import success_response, authentication_required_response

@pytest.fixture(scope="module")
def room_payload(room_api):
    room_data = generate_room()
    return room_data

def test_create_new_room_returns_200(room_api, room_payload, auth_headers):
    response = room_api.create_new_room(room_payload, auth_headers)
    assert_status_code(response, 200)
    assert response.json() == success_response
    rooms_list = room_api.get_all_rooms()
    assert_room_name_exists(rooms_list.json(), room_payload["roomName"])


def test_create_new_room_without_authentication_returns_401(room_api, room_payload):
    response = room_api.create_new_room(room_payload)
    assert_status_code(response, 401)
    assert response.json() == authentication_required_response
