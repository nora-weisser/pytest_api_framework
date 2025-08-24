import pytest
import random
from utils.api_factory.auth_api import AuthAPI
from utils.api_factory.room_api import RoomAPI
from utils.api_factory.booking_api import BookingAPI
from test_data.test_data.room_data import generate_room

@pytest.fixture(scope="module")
def auth_api():
    return AuthAPI()

@pytest.fixture(scope="module")
def room_api():
    return RoomAPI()

@pytest.fixture(scope="module")
def booking_api():
    return BookingAPI()

# --- Authentication ---
@pytest.fixture
def get_token(auth_api):
    response = auth_api.authenticate("admin", "password")
    response_body = response.json()
    token = response_body["token"]
    return token

@pytest.fixture
def get_random_room(room_api):
    response = room_api.get_all_rooms()
    return random.choice(response.json()["rooms"])

@pytest.fixture
def auth_headers(get_token):
    return {'Cookie': f'token={get_token}'}
