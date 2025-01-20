import logging
import os
import json
from typing import List, Dict

# Настройка логгера для модуля `utils`
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Обработчик для записи логов в файл
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Форматтер для логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def read_json_file(file_name: str) -> List[Dict]:
    """
    Читает JSON-файл и возвращает список транзакций.

    :param file_name: Имя файла (относительный путь от корня проекта)
    :return: Список транзакций или пустой список, если файл отсутствует или некорректен
    """
    file_path = os.path.join(os.getcwd(), file_name)
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
