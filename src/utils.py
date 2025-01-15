import os
import json
from typing import List, Dict

def read_json_file(file_name: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список транзакций.

    :param file_name: Имя файла (относительный путь от корня проекта)
    :return: Список транзакций или пустой список, если файл отсутствует или некорректен
    """
    file_path = os.path.join(os.getcwd(), file_name)
    if not os.path.exists(file_path):
        print(f"Файл {file_name} не найден.")
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            print(f"Файл {file_name} не содержит списка.")
            return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка чтения файла {file_name}: {e}")
        return []
