from utils import assertions
import pytest
from utils.schema_validator import response_schema_validator
from test_data.schemas.booking_response import *

@pytest.fixture(scope="module")
def random_room_id(room_api):
    random_room_id = room_api.get_random_room()["roomid"]
    return random_room_id

def test_create_booking_valid_data(random_room_id, booking_api, room_api, get_random_room):
    response = booking_api.create_booking(random_room_id)
    assertions.assert_status_code(response, 200)
    assert response.json() == []

def test_get_booking_by_id(auth_headers, booking_api, random_room_id):
    response = booking_api.get_booking_by_id(random_room_id, auth_headers)
    response_schema_validator(BookingListResponse, response.json())


