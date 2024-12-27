from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по ключу 'state'.

    :param data: Список словарей с банковскими операциями.
    :param state: Значение для фильтрации по ключу 'state' (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только записи с указанным 'state'.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param data: Список словарей с банковскими операциями.
    :param descending: Порядок сортировки (по умолчанию убывание).
    :return: Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda x: datetime.fromisoformat(x.get("date", "")), reverse=descending)
