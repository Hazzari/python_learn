import asyncio
from dataclasses import dataclass
from asyncio import FIRST_COMPLETED, CancelledError

from aiohttp import ClientSession
from loguru import logger

import utils


@dataclass
class Service:
    name: str  # Имя адреса
    url: str  # Адрес API
    ip_field: str  # Поле ip в JSON


# Сайты с Api для получения IP
SERVICE = [
    Service("ipify", "https://api.ipify.org?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
    Service("ipwhois", "http://ipwhois.app/json/", "ip"),
]


async def _fetch(session: ClientSession, url: str) -> dict:
    """ Получаем JSON из Сессии """
    async with session.get(url) as response:
        result = await response.json()
        return result


@utils.timing_dec
async def fetch_ip(service: Service) -> str:
    """Получаем ответ от API """
    async with ClientSession() as session:  # Открываем сессию
        result = await _fetch(session, service.url)  # Получаем JSON
    logger.info("Получил ответ от {}", service.name)

    return result[service.ip_field]  # Возвращаем значение поля ip от  сервиса


async def main():
    # Создаем список задач
    task_list = [asyncio.create_task(fetch_ip(s), name=f'Task-{s.name}') for s in SERVICE]
    # Передаем список задач в  asyncio.wait ( что бы отдать все значения в set нужно использовать *task_list
    # Ждем первый вернувшийся ответ
    done, pending = await asyncio.wait({*task_list}, return_when=FIRST_COMPLETED, timeout=10)

    # Завершаем все оставшиеся задачи
    for y in pending:
        y.cancel()
        try:
            await asyncio.wait_for(y, timeout=10)
        except CancelledError:
            pass

    # Выводим ответ сервера
    for x in done:
        print()
        logger.info("Твой IP  {}", x.result())
        break
    else:
        logger.warning("Значение не получено")


if __name__ == '__main__':
    # Запуск асинхронной функции в новой версии
    asyncio.run(main())
