from utils import apiUtil
from utils.apiUtil import build_url
from TestData.endpoints import ROOM_PATH
from utils.assertions import assert_status_code

def test_get_all_rooms():
    url = build_url(ROOM_PATH)
    response = apiUtil.getAPI(url)

    assert_status_code(response, 200)
    assert isinstance(response.json()['rooms'], list)
