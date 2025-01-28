import json
import logging
import os
from typing import Dict, List

# Настройка логера для модуля utils
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_DIR):
    raise FileNotFoundError(f"Папка {LOG_DIR} отсутствует. Создайте её перед запуском приложения.")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "utils.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def read_json_file(file_name: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список транзакций.

    :param file_name: Имя файла (относительный путь от корня проекта)
    :return: Список транзакций или пустой список, если файл отсутствует или некорректен
    """
    file_path = os.path.join(BASE_DIR, file_name)
    if not os.path.exists(file_path):
        logger.error(f"Файл {file_name} не найден.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Файл {file_name} успешно прочитан. Количество записей: {len(data)}")
                return data
            logger.error(f"Файл {file_name} не содержит списка.")
            return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logger.error(f"Ошибка чтения файла {file_name}: {e}")
        return []
