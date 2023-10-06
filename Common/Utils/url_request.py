""" Функции для работы с запросами к веб-страницам """

import requests

from Logger.config import exception, logger
from typing import Dict
from requests.models import Response
from Common.messages import MES_NO_ACCESS


@logger
@exception
def get_response(url: str) -> Response:
    """ Функция для выполнения запроса по адресу """
    headers: Dict = {'location': url}
    response: Response = requests.get(url, headers=headers)
    return response


@logger
@exception
def get_status(response: Response) -> int:
    """ Функция для проверки запроса по адресу, формирования статуса запроса"""
    if type(response) == Response:
        return response.status_code
    raise Exception(MES_NO_ACCESS)
