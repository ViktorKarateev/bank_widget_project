import os
from typing import List, Dict
from src.file_readers import read_csv_file, read_excel_file
from src.utils import read_json_file
from src.search import search_transactions
from src.category_counter import count_transaction_categories
from src.processing import filter_by_state, sort_by_date

DATA_PATH = "data/"  # Папка с файлами


def load_transactions(file_type: str) -> List[Dict]:
    """
    Загружает транзакции в зависимости от формата файла.
    :param file_type: Тип файла ("json", "csv", "xlsx").
    :return: Список транзакций.
    """
    file_map = {
        "json": "transactions.json",
        "csv": "transactions.csv",
        "xlsx": "transactions.xlsx"
    }

    file_name = file_map.get(file_type)
    if not file_name:
        print("Неверный формат. Используйте json, csv или xlsx.")
        return []

    file_path = os.path.join(DATA_PATH, file_name)

    if file_type == "json":
        return read_json_file(file_path)
    elif file_type == "csv":
        return read_csv_file(file_path)
    elif file_type == "xlsx":
        return read_excel_file(file_path)


def main():
    """
    Основная функция программы.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор типа файла
    file_type = input("Выберите формат файла (json/csv/xlsx): ").strip().lower()
    transactions = load_transactions(file_type)

    if not transactions:
        print("Ошибка загрузки данных.")
        return

    # Фильтрация по статусу
    status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
    transactions = filter_by_state(transactions, status)
    print(f"Операции отфильтрованы по статусу '{status}'.")

    # Сортировка по дате
    if input("Отсортировать операции по дате? Да/Нет: ").strip().lower() == "да":
        order = input("Сортировать по убыванию? (Да/Нет): ").strip().lower() == "да"
        transactions = sort_by_date(transactions, order)

    # Фильтрация по ключевому слову
    if input("Фильтровать по описанию? Да/Нет: ").strip().lower() == "да":
        keyword = input("Введите слово для поиска: ").strip()
        transactions = search_transactions(transactions, keyword)

    # Вывод транзакций
    if transactions:
        print(f"\nВсего операций: {len(transactions)}")
        for txn in transactions:
            print(
                f"{txn.get('date', 'Неизвестно')} | {txn.get('description', 'Нет описания')} | {txn.get('amount', 'Нет суммы')} {txn.get('currency', 'Неизвестно')}")
    else:
        print("Не найдено ни одной транзакции по заданным критериям.")

    # Подсчет категорий
    category_counts = count_transaction_categories(transactions)
    print("\nКоличество операций по категориям:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
