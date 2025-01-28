from datetime import datetime

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-12-10T15:00:00"},
        {"state": "PENDING", "date": "2023-12-09T15:00:00"},
        {"state": "EXECUTED", "date": "2023-12-08T15:00:00"},
    ]

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("PENDING", 1),
    ("CANCELLED", 0),
])
def test_filter_by_state(sample_data, state, expected_count):
    filtered = filter_by_state(sample_data, state)
    assert len(filtered) == expected_count
    assert all(item["state"] == state for item in filtered)

@pytest.mark.parametrize("descending, expected_dates", [
    (True, ["2023-12-10", "2023-12-09", "2023-12-08"]),
    (False, ["2023-12-08", "2023-12-09", "2023-12-10"]),
])
def test_sort_by_date(sample_data, descending, expected_dates):
    sorted_data = sort_by_date(sample_data, descending)
    dates = [datetime.fromisoformat(item["date"]).strftime("%Y-%m-%d") for item in sorted_data]
    assert dates == expected_dates