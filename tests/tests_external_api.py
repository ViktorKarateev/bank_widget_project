import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub
from dotenv import load_dotenv

load_dotenv()

@patch("src.external_api.requests.get")
def test_convert_to_rub_usd_currency(mock_get):
    """Тест конвертации из USD в RUB."""
    mock_get.return_value.json.return_value = {"rates": {"RUB": 75.0}}
    mock_get.return_value.status_code = 200

    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result == 7500.0


@patch("src.external_api.requests.get")
def test_convert_to_rub_missing_key(mock_get):
    """Тест отсутствующего курса RUB."""
    mock_get.return_value.json.return_value = {}
    mock_get.return_value.status_code = 200

    transaction = {"amount": 100, "currency": "USD"}

    with pytest.raises(ValueError, match="Не удалось получить курс валют."):
        convert_to_rub(transaction)


@patch("src.external_api.requests.get", side_effect=Exception("Ошибка сети"))
def test_convert_to_rub_api_error(mock_get):
    """Тест ошибки сети."""
    transaction = {"amount": 100, "currency": "USD"}

    with pytest.raises(ValueError, match="Ошибка при запросе к API: Ошибка сети"):
        convert_to_rub(transaction)
