import pytest
from src.generators import filter_by_currency

@pytest.mark.parametrize("transactions, currency, expected_count", [
    ([{"operationAmount": {"currency": {"code": "USD"}}}], "USD", 1),
    ([{"operationAmount": {"currency": {"code": "RUB"}}}], "USD", 0),
    ([], "USD", 0),
])
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count



from src.generators import transaction_descriptions

def test_transaction_descriptions():
    transactions = [
        {"description": "Test 1"},
        {"description": "Test 2"},
        {"description": "Test 3"},
    ]
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Test 1"
    assert next(generator) == "Test 2"
    assert next(generator) == "Test 3"


from src.generators import card_number_generator

@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
])
def test_card_number_generator(start, stop, expected):
    generator = card_number_generator(start, stop)
    assert list(generator) == expected




