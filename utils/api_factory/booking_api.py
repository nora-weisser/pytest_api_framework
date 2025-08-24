from utils.api_factory.api_util import APIClient
from test_data.endpoints import BOOKING_PATH
from test_data.test_data.booking_data import valid_booking_data
import allure

class BookingAPI(APIClient):
    path = BOOKING_PATH

    def __init__(self):
        super().__init__()

    @allure.step('Creating a booking')
    def create_booking(self, room_id: str, add_headers: dict = None):
        """
        Creates a booking using the provided room_id and booking data function.
        booking_data_func: A function that returns the booking payload, e.g., valid_booking_data(room_id)
        """
        payload = valid_booking_data(room_id)
        response = self.post(self.path, body=payload, add_headers=add_headers)
        return response

    @allure.step('Get Booking By Id')
    def get_booking_by_id(self, random_room_id: str, add_headers: dict = None):
        response = self.get(f"{self.path}?roomid={random_room_id}", add_headers=add_headers)
        return response