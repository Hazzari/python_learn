import logging

from dotenv import dotenv_values

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

# # ------ || старт настройка бота
logging.basicConfig(level=logging.DEBUG)

# Импорт переменных среды
config = dotenv_values('.bot.env')
TOKEN = config['TOKEN']

# Подключаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)


# # ------ || конец настройки бота


@dp.message_handler()
async def echo_message(message: types.Message):
    return await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
