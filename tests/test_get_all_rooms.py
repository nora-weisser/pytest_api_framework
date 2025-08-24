from utils.assertions import assert_status_code
from utils.schema_validator import response_schema_validator
from test_data.schemas.room_response import RoomListResponse

def test_get_all_rooms_returns_list(room_api):
    response = room_api.get_all_rooms()
    assert_status_code(response, 200)
    response_schema_validator(RoomListResponse, response.json())
