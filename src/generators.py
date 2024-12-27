from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по указанной валюте.

    :param transactions: Список транзакций.
    :param currency: Код валюты для фильтрации (например, "USD").
    :return: Итератор по транзакциям в указанной валюте.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Возвращает описания транзакций.

    :param transactions: Список транзакций.
    :return: Итератор с описаниями транзакций.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор для создания номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона.
    :param stop: Конечное значение диапазона.
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        formatted_number = f"{number:016}"  # Форматируем в строку длиной 16 с ведущими нулями
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
