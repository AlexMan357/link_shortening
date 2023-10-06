""" Модуль с конфигурацией логгера """

import time
from datetime import datetime
from typing import Callable, Any
from Logger.helper import logger_dump_data, check_logger_file


def logger(function: Callable) -> Callable:
    """ Декоратор, логгирующий работу функций """
    def wrapper(* args, **kwargs) -> Any:
        check_logger_file()
        started_at: float = time.time()
        result: Callable = function(*args, **kwargs)
        ended_at: float = time.time()
        run_time: float = round(ended_at - started_at)

        data: str = ' '.join([
            str(datetime.now()),
            str(function),
            str(args),
            str(result),
            str(run_time)
        ])

        logger_dump_data(data=data)

        return result
    return wrapper


def exception(function: Callable) -> Callable:
    """ Декоратор, перехватывающий ошибки функций """
    def wrapper(*args, **kwargs) -> Any:
        try:
            result: Callable = function(*args, **kwargs)
            data: str = str(function.__name__)

            logger_dump_data(data=data)
            return result
        except Exception as exc:
            return exc
    return wrapper
