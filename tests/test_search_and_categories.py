import pytest
from src.search import search_transactions
from src.category_counter import count_transaction_categories

@pytest.fixture
def sample_transactions():
    return [
        {"description": "Покупка в магазине", "status": "EXECUTED", "currency": "RUB", "amount": 100},
        {"description": "Перевод другу", "status": "PENDING", "currency": "USD", "amount": 50},
        {"description": "Оплата услуг", "status": "EXECUTED", "currency": "RUB", "amount": 200},
        {"description": "Покупка в интернете", "status": "EXECUTED", "currency": "RUB", "amount": 150},
    ]

def test_search_transactions(sample_transactions):
    """Тест поиска транзакций по ключевому слову."""
    result = search_transactions(sample_transactions, "Покупка")
    assert len(result) == 2  # Две транзакции содержат слово "Покупка"
    assert all("Покупка" in txn["description"] for txn in result)

def test_count_transaction_categories(sample_transactions):
    """Тест подсчета категорий транзакций."""
    result = count_transaction_categories(sample_transactions)
    assert result["Покупка в магазине"] == 1
    assert result["Покупка в интернете"] == 1
    assert result["Перевод другу"] == 1
    assert result["Оплата услуг"] == 1
