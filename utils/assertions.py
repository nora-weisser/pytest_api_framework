import allure

@allure.step('Asserting Response Status code')
def assert_status_code(response, expected_status: int):
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Expected {expected_status} but got {actual_status}. "
        f"Response body: {getattr(response, 'text', '')}"
)

@allure.step('Asserts that newly created room is present in the list of rooms')
def assert_room_name_exists(rooms_list, room_name):
    assert any(room["roomName"] == room_name for room in rooms_list["rooms"]), f"Room name '{room_name}' not found!"
