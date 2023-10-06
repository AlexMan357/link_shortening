""" Модуль с функциями для логгера """

import os
from Common.settings import STORAGE_PATHS
from Common.messages import MES_ERROR
path = STORAGE_PATHS[1]


def logger_dump_data(data: str):
    """ Функция для записи в файл .txt результатов логгирования"""
    with open(path, "a", encoding='UTF8') as write_file:
        write_file.write('\n')
        write_file.write(data)


def logger_get_filesize() -> int:
    """ Функция определения размера файла """
    return os.path.getsize(path)


def check_logger_file() -> None:
    """ Функция очистки файла """
    if logger_get_filesize() > 100 * 1024:
        try:
            f = open(path, 'w')
            f.close()
        except Exception as exc:
            print(MES_ERROR, exc)
