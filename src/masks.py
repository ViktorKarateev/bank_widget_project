import logging

# Настройка логгера для модуля `masks`
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Обработчик для записи логов в файл
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

# Форматтер для логов
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Маскированный номер карты в виде строки.
    """
    try:
        card_number_str = str(card_number)
        masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.info(f"Маскирован номер карты: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Ошибка маскирования карты: {e}")
        raise


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Маскированный номер счета в виде строки.
    """
    try:
        account_number_str = str(account_number)
        masked_number = f"**{account_number_str[-4:]}"
        logger.info(f"Маскирован номер счета: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Ошибка маскирования счета: {e}")
        raise
