from utils.api_factory.api_util import APIClient
import allure
import random
from test_data import endpoints

class RoomAPI(APIClient):
    path = endpoints.ROOM_PATH

    def __init__(self):
        super().__init__()

    @allure.step('Get All Rooms')
    def get_all_rooms(self):
        response = self.get(self.path)
        return response

    @allure.step('Get Random Room From the List of Rooms')
    def get_random_room(self):
        response = self.get_all_rooms()
        return random.choice(response.json()["rooms"])

    @allure.step('Create a New Room')
    def create_new_room(self, room_data, auth_headers=None):
        response = self.post(self.path, room_data, auth_headers)
        return response