import requests
import os
from typing import Dict


def convert_to_rub(transaction: Dict[str, float | str]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции.
        Пример: {"amount": 100, "currency": "USD"}
    :return: Сумма в рублях (float).
    :raises ValueError: Если API-ключ отсутствует, курс валют не найден или запрос завершился ошибкой.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в переменных окружения.")

    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    headers = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        rates = response.json().get("rates", {})
        rub_rate = rates.get("RUB")

        if not rub_rate:
            raise ValueError("Не удалось получить курс валют.")

        return float(amount) * rub_rate
    except Exception as e:
        raise ValueError(f"Ошибка при запросе к API: {e}")

