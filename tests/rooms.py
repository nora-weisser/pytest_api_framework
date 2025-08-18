from utils import apiUtil
from utils.myconfigparser import getURL
from urllib.parse import urljoin
from TestData.endpoints import ROOM_PATH

def test_get_all_rooms():
    url = urljoin(getURL(), ROOM_PATH)
    response = apiUtil.getAPI(url)
    assert response.status_code == 200
