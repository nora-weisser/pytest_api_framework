from utils import api_util
from utils.assertions import assert_status_code
from utils.schema_validator import response_schema_validator
from TestData.schemas.room_response import RoomListResponse


def test_get_all_rooms_returns_list(room_url):
    response = api_util.get_api(room_url)
    assert_status_code(response, 200)
    response_schema_validator(RoomListResponse, response.json())
