import logging
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования вызова функций, их аргументов, результата и ошибок.

    :param filename: Имя файла для записи логов. Если не задано, логи выводятся в консоль.
    :return: Обёрнутая функция с логированием.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            logger.handlers.clear()

        handler = logging.FileHandler(filename) if filename else logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger.info("Calling %s with args: %s, kwargs: %s", func.__name__, args, kwargs)
            try:
                result = func(*args, **kwargs)
                logger.info("%s returned %s", func.__name__, result)
                return result
            except Exception as error:
                logger.error(
                    "%s raised %s: %s. Inputs: args=%s, kwargs=%s",
                    func.__name__,
                    type(error).__name__,
                    error,
                    args,
                    kwargs,
                )
                raise

        return wrapper

    return decorator
