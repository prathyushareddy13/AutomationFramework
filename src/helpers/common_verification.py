def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed, Status code is not matching"


def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed, since key is not matching"


def verify_json_key_not_null(key):
    assert key != 0, "Failed, Key is null"


def verify_json_key_gr_zero(key):
    assert key > 0, "Failed, Key is not > 0"