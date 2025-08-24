from utils.api_factory.api_util import APIClient
import allure
from test_data import endpoints

class AuthAPI(APIClient):
    path = endpoints.LOGIN_PATH

    def __init__(self):
        super().__init__()

    @allure.step('Get All Rooms')
    def authenticate(self, username: str, password: str):
        payload = {
            "username": username,
            "password": password
        }
        response = self.post(self.path, payload)
        return response