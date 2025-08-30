# Pytest API Framework

A modular API testing framework built with Pytest, designed for testing REST APIs efficiently with reusable clients, schema validation, and rich reporting.

I use the [Restful Booker Platform](https://github.com/mwinteringham/restful-booker-platform) as the system under test:
- [Live API Endpoint](https://github.com/mwinteringham/restful-booker-platform)
- [GitHub Repository](https://github.com/mwinteringham/restful-booker-platform)
- [Postman Collection](https://www.postman.com/automation-in-testing/restful-booker-collections/collection/ci13ds3/restful-booker-platform)

## Features

1. Reusable API client classes (GET, POST, etc.)
2. Centralized endpoint and test data management
3. JSON schema validation using Pydantic library
4. Pytest fixtures and parameterized test support
5. Allure reporting integration

## Setup
```
git clone git@github.com:nora-weisser/pytest_api_framework.git
cd pytest_api_framework
poetry install
```

## Run Tests
```
poetry run pytest
```

## Run Test Cases With Allure Report
```
pytest --alluredir=allure-results
allure serve allure-results
```
## Implemented Test Cases

### Authentication Tests

#### `test_login`
- **Description**: Verifies the login API using multiple username/password combinations.
- **Test Scenarios**:
  - Valid credentials → Expect `200 OK` and valid response schema
  - Invalid password → Expect `401 Unauthorized`
  - Unknown user → Expect `401 Unauthorized`
  - Empty credentials → Expect `401 Unauthorized`

---

### Booking Tests

#### `test_create_booking_valid_data`
- **Description**: Sends a valid booking request using a random available room.
- **Validations**:
  - Status code is `200`
  - Response body is an empty list (`[]`) 

#### `test_get_booking_by_id`
- **Description**: Retrieves booking information by room ID with valid authentication.
- **Validations**:
  - Status code is `200`
  - Response schema matches `BookingListResponse`

---

### Room Management Tests

#### `test_create_new_room_returns_200`
- **Description**: Creates a new room with valid data and authentication.
- **Validations**:
  - Status code is `200`
  - Response matches `success_response`
  - Newly created room appears in the room list

#### `test_create_new_room_without_authentication_returns_401`
- **Description**: Tries to create a room without authentication.
- **Validations**:
  - Status code is `401 Unauthorized`
  - Response matches `authentication_required_response`

#### `test_get_all_rooms_returns_list`
- **Description**: Fetches all rooms from the system.
- **Validations**:
  - Status code is `200`
  - Response schema matches `RoomListResponse`
