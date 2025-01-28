import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    (1234567812345678, "1234 56** **** 5678"),  # Обычный случай
    (12345678, "1234 56** **** 5678"),  # Короткий номер (предположим, что функция обрабатывает его корректно)
    (0, "0 ** **** 0"),  # Граничный случай для пустой строки
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    (98765432189, "**2189"),  # Обычный случай
    (1234, "**1234"),  # Короткий номер счета
    (0, "**0"),  # Граничный случай для пустой строки
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

