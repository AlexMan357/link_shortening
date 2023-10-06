""" Модуль общих настроек """

import os


def path_generate(filename: str) -> str:
    """ Функция генерации пути для исполняемого файла main.py в корне проекта """
    return os.path.join(
                         os.path.abspath(STORAGE_TEMPLATE_DIRECTORY),
                         filename
                        )


STORAGE_TEMPLATE_DIRECTORY = 'Storage/templates'

STORAGE_PATHS = [
    path_generate(filename='data_file.json'),
    path_generate(filename='log.txt')
]
