""" Функции для работы с хранилищем данных """

import json

from Common.messages import MES_NO_FOUND
from Common.settings import STORAGE_PATHS
from Logger.config import exception, logger
from typing import Dict, Any


@logger
@exception
def dump_data(data: Dict, flag: int) -> None:
    """ Функция для загрузки данных в файл json"""
    with open(STORAGE_PATHS[flag], "w", encoding='UTF8') as write_file:
        json.dump(data, write_file)


@logger
@exception
def load_data(flag: int) -> Dict:
    """ Функция для загрузки данных из файла json"""
    with open(STORAGE_PATHS[flag], "r", encoding='UTF8') as read_file:
        return json.load(read_file)


@logger
@exception
def get_key(data: Dict) -> str:
    """ Функция нахождения ключа одного элементы словаря """
    for key in data.keys():
        alias: str = key
        return alias


@logger
@exception
def get_homepage_name(data, alias):
    """ Функция нахождения домашнего адреса в словаре данных data """
    homepage = data.get(alias, {}).get('homepage', {})
    if homepage:
        return homepage
    raise Exception(MES_NO_FOUND)


@logger
@exception
def get_short_and_url(data: Dict, short_url) -> Any:
    """ Функция нахождения короткого и стандарстного адреса в словаре данных data """
    for key, value in data.items():
        if short_url in value.values():
            return value['url'], value['short_url']
    return MES_NO_FOUND, MES_NO_FOUND


@logger
@exception
def get_alias_and_homepage_all(data: Dict) -> Any:
    """ Функция извлекает все данные из data в формате псевдоним, домашняя страница """
    result = []
    for key, value in data.items():
        result.append((key, value['homepage']))
    if result:
        return result
    return MES_NO_FOUND


@logger
@exception
def get_short_and_url_all(data: Dict) -> Any:
    """ Функция извлекает все данные из data в формате короткий, стандартный адреса """
    result = []
    for value in data.values():
        result.append((value['short_url'], value['url']))
    if result:
        return result
    return MES_NO_FOUND


@logger
@exception
def get_alias_from_db(data: Dict, alias) -> Any:
    """ Функция поиска ключа data по заданнному псевдониму alias """
    for key in data.keys():
        if key == alias:
            return key
    return MES_NO_FOUND
