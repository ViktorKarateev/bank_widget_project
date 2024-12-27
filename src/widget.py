from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета.

    :param data: Строка с типом и номером карты/счета.
    :return: Строка с замаскированным номером.
    """
    if "Счет" in data:
        account_number = data.split()[-1]
        return f"Счет {get_mask_account(int(account_number))}"
    else:
        card_type, card_number = " ".join(data.split()[:-1]), data.split()[-1]
        return f"{card_type} {get_mask_card_number(int(card_number))}"


def get_date(date_str: str) -> str:
    """
    Преобразует строку даты из формата 'YYYY-MM-DDTHH:MM:SS.ssssss'
    в формат 'ДД.ММ.ГГГГ'.

    :param date_str: Дата в формате '2024-03-11T02:26:18.671407'.
    :return: Дата в формате '11.03.2024'.
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
