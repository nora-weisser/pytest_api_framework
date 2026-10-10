# Pytest API Framework

A layered API test framework in Python: reusable API clients, Pydantic schema validation, Faker-generated test data and Allure reporting, built around pytest fixtures.

The system under test is the [Restful Booker Platform](https://github.com/mwinteringham/restful-booker-platform), a hotel booking API with authentication, rooms and bookings. It runs live at [automationintesting.online](https://automationintesting.online), and there is also a [Postman collection](https://www.postman.com/automation-in-testing/restful-booker-collections/collection/ci13ds3/restful-booker-platform).

## Why it's built this way

- **Tests read like specifications.** Each test says what it checks; HTTP details live in the API clients, so a changed endpoint means one edit, not twenty.
- **Responses are validated against Pydantic models**, so a missing or renamed field fails the test even when the status code is still `200`.
- **Fixtures handle setup.** Authentication, API clients and test data come from `conftest.py`, so tests don't repeat login or lookup code.
- **Data is generated, not hard-coded.** Rooms and bookings are built with Faker, so repeated runs don't collide on the same records.

## Project structure

```
config/qa.ini                 environment settings (base URL), read by utils/myconfigparser.py
utils/
  api_factory/                one client per API area, sharing a common request layer
    api_util.py               base HTTP client
    auth_api.py               login
    room_api.py               rooms
    booking_api.py            bookings
  schema_validator.py         validates responses against Pydantic models
  assertions.py               shared assertions
test_data/
  endpoints.py                all endpoint paths in one place
  schemas/                    Pydantic models for requests and responses
  test_data/                  Faker-based builders for rooms and bookings
  expected_responses.py       expected bodies for error and success cases
tests/
  conftest.py                 fixtures: API clients, auth token, auth headers, a random room
  login/  rooms/  bookings/   tests grouped by API area
```

## What's tested

| Area | Test | Checks |
| --- | --- | --- |
| Authentication | `test_login` (parametrized) | Valid credentials return `200` and a valid schema; wrong password, unknown user and empty credentials return `401` |
| Rooms | `test_create_new_room_returns_200` | A room created with valid data appears in the room list |
| Rooms | `test_create_new_room_without_authentication_returns_401` | Creating a room without a token is rejected with the expected error body |
| Rooms | `test_get_all_rooms_returns_list` | The room list matches `RoomListResponse` |
| Bookings | `test_create_booking_valid_data` | A booking for a random available room is accepted |
| Bookings | `test_get_booking_by_id` | Bookings for a room match `BookingListResponse` |

## Getting started

Requires Python 3.12+ and [Poetry](https://python-poetry.org/).

```bash
git clone https://github.com/nora-weisser/pytest_api_framework.git
cd pytest_api_framework
poetry install
```

Run the tests:

```bash
poetry run pytest
```

With an Allure report (needs the [Allure CLI](https://allurereport.org/docs/install/)):

```bash
poetry run pytest --alluredir=allure-results
allure serve allure-results
```

To test against another environment, change the base URL in `config/qa.ini`.

## Related

- [Blog: TechNotes](https://noraweisser.com) — posts on API testing, schema validation and test data
- [api_testing_with_pactumjs](https://github.com/nora-weisser/api_testing_with_pactumjs) — the same ideas in JavaScript with PactumJS
