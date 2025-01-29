import re
from typing import List, Dict

def search_transactions(transactions: List[Dict], keyword: str) -> List[Dict]:
    """
    Поиск транзакций по описанию с использованием регулярных выражений.
    :param transactions: список транзакций (список словарей)
    :param keyword: строка для поиска в описании транзакции
    :return: список словарей с найденными транзакциями
    """
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    return [txn for txn in transactions if pattern.search(txn.get("description", ""))]