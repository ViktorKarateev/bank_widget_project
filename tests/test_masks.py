from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account(1234567890123456) == "**3456"
