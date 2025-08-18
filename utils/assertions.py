def assert_status_code(response, expected_status: int):
    actual_status = response.status_code
    assert actual_status == expected_status, (
        f"Expected {expected_status} but got {actual_status}. "
        f"Response body: {getattr(response, 'text', '')}"
)