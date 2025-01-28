from collections import Counter
from typing import List, Dict

def count_transaction_categories(transactions: List[Dict]) -> Dict[str, int]:
    """
    Подсчет количества транзакций по категориям.
    :param transactions: список транзакций (список словарей)
    :return: словарь с количеством операций в каждой категории
    """
    categories = [txn.get("description", "Unknown") for txn in transactions]
    return dict(Counter(categories))
