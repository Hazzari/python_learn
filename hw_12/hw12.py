"""
https://jsonplaceholder.typicode.com

/posts	100 posts
/comments	500 comments
/albums	100 albums
/photos	5000 photos
/todos	200 todos
/users	10 users


Асинхронная работа с сетью
написать скрипт,
который при помощи асинхронного клиента
обращается к открытому апи (например, jsonplaceholder) и
выводит оттуда информацию

создать модели для объектов,

которые тянутся с открытого апи

записать вытянутые модели в БД


скрипт для стягивания данных
и записи в БД реализован в асинхронном виде


# - обращение к api
# - собирает информацию
# - выводит информацию
# - создаем модели
# - запись данных модели в базу данных

"""

import asyncio
# from dataclasses import dataclass
from pprint import pprint

from aiohttp import ClientSession
from tortoise import Tortoise, run_async, fields
from tortoise.models import Model, ModelMeta

# from loguru import logger

URL = 'https://jsonplaceholder.typicode.com/posts/'


async def _fetch(session: ClientSession, url: str) -> dict:
    """ Получаем JSON из Сессии """
    async with session.get(url) as response:
        result = await response.json()
        return result


async def fetch_api_data():
    """Получаем ответ от API """
    async with ClientSession() as session:  # Открываем сессию
        result = await _fetch(session, URL)  # Получаем JSON
    return result  # Возвращаем значение поля ip от  сервиса


fetch_api = asyncio.run(fetch_api_data())[0]


# print(fetch)


class MyMetaclass(ModelMeta):
    def __new__(mcs, name, bases, dct):
        new_cls = super().__new__(mcs, name, bases, dct)

        return new_cls


dict_cLass = dict()
for x, v in fetch_api.items():
    dict_cLass[x] = v
print(dict_cLass)

myclass = MyMetaclass('NameClass', (Model,), dict_cLass)

print(myclass.title)
