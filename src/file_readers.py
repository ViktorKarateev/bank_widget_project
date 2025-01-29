import os
import pandas as pd
from typing import List, Dict


def read_csv_file(file_name: str) -> List[Dict]:
    """
    Считывает данные из CSV-файла и возвращает список транзакций.

    :param file_name: Имя файла (относительный путь от корня проекта).
    :return: Список словарей с данными транзакций.
    """
    file_path = os.path.join(os.getcwd(), "data", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    try:
        df = pd.read_csv(file_path, delimiter=";", encoding="utf-8")  # ✅ Добавлен delimiter=";"
        print("🔍 Первые 5 записей из CSV:", df.head(5).to_dict(orient="records"))  # Отладка
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_excel_file(file_name: str) -> List[Dict]:
    """
    Считывает данные из Excel-файла и возвращает список транзакций.

    :param file_name: Имя файла (относительный путь от корня проекта).
    :return: Список словарей с данными транзакций.
    """
    file_path = os.path.join(os.getcwd(), "data", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    try:
        df = pd.read_excel(file_path, engine="openpyxl", dtype=str)  # ✅ Добавлен dtype=str
        print("🔍 Первые 5 записей из Excel:", df.head(5).to_dict(orient="records"))  # Отладка
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")
