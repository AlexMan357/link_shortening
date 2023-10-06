""" Функции для работы с регулярными выражениями """

from Common.regex_rules import (
    REG_ALIAS,
    REG_TAIL_URL,
    REG_LETTERS,
    REG_SPACE, STRING_HOMEPAGE, REG_CHECK_STRING,
)
from Logger.config import exception, logger
import re
import random
from typing import List, Dict
from Common.messages import MES_WRONG_URL


@logger
@exception
def get_alias(url: str) -> str:
    """ Функция для нахождения псевдонима страницы url """
    result: List = re.findall(REG_ALIAS, url)
    alias: str = result[0]
    return alias


@logger
@exception
def get_tail_url(url: str) -> str:
    """ Функция для нахождения списка букв в хвостовой части адреса url """
    tail_url: List = re.findall(REG_TAIL_URL, url)
    tail_letters: str = re.sub(REG_LETTERS, '', *tail_url)
    return tail_letters


@logger
@exception
def get_homepage_url(alias: str) -> str:
    """ Функция для нахождения домашней страницы """
    home_page_url: str = re.sub(REG_SPACE, alias, STRING_HOMEPAGE)
    return home_page_url


@logger
@exception
def get_short_url(url: str) -> Dict:
    """ Функция для нахождения короткого адреса """
    if check_url(url):
        alias: str = get_alias(url)
        tail_letters: str = get_tail_url(url)
        homepage: str = get_homepage_url(alias)

        short_url = re.compile(f'{alias[:3]}'
                               f'.{"".join(random.choices(alias, k=2))}'
                               f'/{"".join(random.choices(tail_letters, k=4))}'
                               )
        short_url = short_url.pattern

        data: Dict = {
            alias: {
                'short_url': short_url,
                'homepage': homepage,
                'url': url
            }
        }

        return data
    else:
        raise Exception(MES_WRONG_URL)


@logger
@exception
def check_url(url: str) -> bool:
    """ Функция для проверки строки url """
    url = remove_space(url)
    pattern = re.compile(REG_CHECK_STRING)
    match = pattern.search(url)
    if match is not None:
        return True
    return False


@logger
@exception
def remove_space(url: str) -> str:
    """ Функция для удаления пробельных символов строки url """
    return re.sub(REG_SPACE, '', url)
