import os
import pandas as pd
from typing import List, Dict
from src.file_readers import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.search import search_transactions
from src.category_counter import count_transaction_categories
from src.processing import sort_by_date

# Определяем путь к папке с данными
DATA_PATH = os.path.join(os.getcwd(), "data")


def load_transactions(file_type: str) -> List[Dict]:
    """
    Загружает транзакции из файла заданного типа.
    """
    file_map = {
        "json": "operations.json",
        "csv": "transactions.csv",
        "xlsx": "transactions_excel.xlsx"
    }

    file_name = file_map[file_type]
    file_path = os.path.join(DATA_PATH, file_name)

    print(f"Загружаем файл: {file_path}")

    if not os.path.exists(file_path):
        print(f"Ошибка: Файл {file_path} не найден!")
        return []

    if file_type == "json":
        return read_json_file(file_path)
    elif file_type == "csv":
        return read_csv_file(file_path)
    elif file_type == "xlsx":
        return read_excel_file(file_path)
    return []


def get_filtered_status(transactions: List[Dict]) -> List[Dict]:
    """
    Фильтрует транзакции по выбранному пользователем статусу.
    """
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in valid_statuses:
            filtered_transactions = [txn for txn in transactions if str(txn.get("state", "")).upper() == status]
            print(f"После фильтрации по статусу '{status}' осталось {len(filtered_transactions)} транзакций.")
            return filtered_transactions
        print("Ошибка: Некорректный статус. Попробуйте снова.")


def get_yes_no(prompt: str) -> bool:
    """
    Запрашивает у пользователя "Да" или "Нет", пока не будет введен корректный ответ.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"да", "нет"}:
            return answer == "да"
        print("Ошибка: Введите 'Да' или 'Нет'.")


def main():
    """
    Основная функция программы.
    """
    print("Добро пожаловать в программу работы с банковскими транзакциями.")

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

    if not transactions:
        print("Ошибка загрузки данных.")
        return

    transactions = get_filtered_status(transactions)

    if get_yes_no("Отсортировать операции по дате? Да/Нет: "):
        order = get_yes_no("Отсортировать по убыванию? Да/Нет: ")
        transactions = sort_by_date(transactions, order)

    if get_yes_no("Выводить только рублевые транзакции? Да/Нет: "):
        transactions = [txn for txn in transactions if txn.get("currency_code", "").upper() == "RUB"]
    print(f"После фильтрации по валюте осталось {len(transactions)} транзакций.")

    if get_yes_no("Отфильтровать список транзакций по слову в описании? Да/Нет: "):
        keyword = input("Введите слово для фильтрации: ").strip()
        transactions = search_transactions(transactions, keyword)

    print("\nИтоговый список транзакций:")
    if transactions:
        for txn in transactions[:10]:
            amount = txn.get("amount") or txn.get("operationAmount", {}).get("amount", "Нет суммы")
            currency = txn.get("currency_code") or txn.get("operationAmount", {}).get("currency", {}).get("code",
                                                                                                          "Неизвестно")
            print(f"{txn.get('date', 'Неизвестно')} | {txn.get('description', 'Нет описания')}")
            print(f"Сумма: {amount} {currency}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под условия фильтрации.")

    category_counts = count_transaction_categories(transactions)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
