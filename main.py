import os
from typing import List, Dict
from src.file_readers import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.search import search_transactions
from src.category_counter import count_transaction_categories
from src.processing import sort_by_date

DATA_PATH = "data"  # Папка с файлами


def load_transactions(file_type: str) -> List[Dict]:
    """
    Загружает транзакции в зависимости от формата файла.
    :param file_type: Тип файла ("json", "csv", "xlsx").
    :return: Список транзакций.
    """
    file_map = {
        "json": "operations.json",
        "csv": "transactions.csv",
        "xlsx": "transactions_excel.xlsx"
    }

    file_path = file_map[file_type]

    print(f"Загружаем файл: {file_path}")  # Отладочный вывод

    if file_type == "json":
        return read_json_file(file_path)
    elif file_type == "csv":
        return read_csv_file(file_path)
    elif file_type == "xlsx":
        return read_excel_file(file_path)


def get_filtered_status(transactions: List[Dict]) -> List[Dict]:
    """
    Фильтрует транзакции по статусу, который вводит пользователь.
    :param transactions: список транзакций
    :return: отфильтрованный список
    """
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in valid_statuses:
            filtered_transactions = [txn for txn in transactions if str(txn.get("state", "")).upper() == status]
            print(f"Операции отфильтрованы по статусу '{status}'.")
            print(f"🔍 После фильтрации по статусу осталось {len(filtered_transactions)} транзакций.")
            return filtered_transactions
        else:
            print(f"Ошибка: статус '{status}' недоступен. Попробуйте снова.")


def main():
    """
    Основная функция программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input("Введите номер пункта: ").strip()
        if choice in {"1", "2", "3"}:
            file_type = {"1": "json", "2": "csv", "3": "xlsx"}[choice]
            print(f"Для обработки выбран {file_type.upper()}-файл.")
            break
        print("Ошибка: выберите 1, 2 или 3.")

    transactions = load_transactions(file_type)
    print(f"🔍 Загружено {len(transactions)} транзакций до фильтрации.")
    for txn in transactions[:5]:
        print(txn)

    if not transactions:
        print("Ошибка загрузки данных.")
        return

    # Фильтрация по статусу
    transactions = get_filtered_status(transactions)

    # Сортировка по дате
    if input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower() == "по убыванию"
        transactions = sort_by_date(transactions, order)

    # Фильтрация по валюте
    if input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower() == "да":
        transactions = [txn for txn in transactions if txn.get("currency", "").upper() == "RUB"]
    print(f"🔍 После фильтрации по валюте осталось {len(transactions)} транзакций.")

    # Фильтрация по описанию
    if input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower() == "да":
        keyword = input("Введите слово для фильтрации: ").strip()
        transactions = search_transactions(transactions, keyword)

    # Вывод транзакций
    print("\nРаспечатываю итоговый список транзакций...")
    if transactions:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for txn in transactions:
            print(
                f"{txn.get('date', 'Неизвестно')} {txn.get('description', 'Нет описания')}")
            print(f"Сумма: {txn.get('amount', 'Нет суммы')} {txn.get('currency', 'Неизвестно')}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

    # Подсчет категорий
    category_counts = count_transaction_categories(transactions)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
