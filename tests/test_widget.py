import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("data, expected", [
    ("Счет 12345678", "Счет **5678"),
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
])
def test_mask_account_card(data, expected):
    assert mask_account_card(data) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-01-01T00:00:00", "01.01.2023"),
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected