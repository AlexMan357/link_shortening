""" Модуль с регулярными выражениями """

REG_ALIAS = r'(?:https://|www.)+(.*?).ru'
REG_TAIL_URL = r'.ru(.*)'
REG_LETTERS = r'[^a-z]'
REG_SPACE = r'\s'
REG_SHORT_URL = './'
STRING_HOMEPAGE = 'https://www. .ru'
REG_CHECK_STRING = r'(?:https://|www.)+\w+.ru\S+'
