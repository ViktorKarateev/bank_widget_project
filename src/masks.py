import logging
import os

# Настройка логера для модуля masks
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOG_DIR):
    raise FileNotFoundError(f"Папка {LOG_DIR} отсутствует. Создайте её перед запуском приложения.")

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, "masks.log"), mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Маскированный номер карты в виде строки.
    """
    card_number_str = str(card_number)
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.info(f"Успешно замаскирован номер карты: {masked_number}")
    return masked_number

def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Маскированный номер счета в виде строки.
    """
    account_number_str = str(account_number)
    masked_number = f"**{account_number_str[-4:]}"
    logger.info(f"Успешно замаскирован номер счета: {masked_number}")
    return masked_number
