def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер карты в формате XXXX XX** **** XXXX.

    :param card_number: Номер карты в виде числа.
    :return: Маскированный номер карты в виде строки.
    """
    card_number_str = str(card_number)  # Преобразуем число в строку
    masked_number = (
        f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    )
    return masked_number


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер счета в формате **XXXX.

    :param account_number: Номер счета в виде числа.
    :return: Маскированный номер счета в виде строки.
    """
    account_number_str = str(account_number)  # Преобразуем число в строку
    masked_number = f"**{account_number_str[-4:]}"
    return masked_number
