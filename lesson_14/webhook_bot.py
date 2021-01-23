import logging
from datetime import datetime
from pathlib import Path
from random import randint

from dotenv import dotenv_values

from aiogram import Bot, types
from aiogram.types import Message, ContentTypes
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

config = dotenv_values('.bot.env')
TOKEN = config['TOKEN']
WEBHOOK_HOST = config['WEBHOOK_HOST']

# webhook settings
WEBHOOK_PATH = f"/webhook/{TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3000

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

BOT_DIR = Path(__file__).resolve().parent

STICKERS_DIR: Path = BOT_DIR / "stickers"
STICKERS_DIR.mkdir(exist_ok=True)


# Сообщения
@dp.message_handler()
async def echo(message: Message):
    # Regular request
    # await bot.send_message(message.chat.id, message.text)

    # or reply INTO webhook
    return SendMessage(message.chat.id, message.text)


# Фотографии
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def echo_photo(message: Message):
    return await message.answer_photo(message.photo[-1].file_id,
                                      caption=f'Твоя подпись: {message.caption}')


# Стикеры и Анимация
@dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
async def forward_any_sticker(message: Message):
    file_id = message.sticker.file_id
    await bot.download_file_by_id(
        file_id=file_id,
        destination=STICKERS_DIR / f"sticker_{datetime.now()}_{randint(0, 100)}."
                                   f"{'TGS' if message.sticker.is_animated else 'webp'}",
    )
    return await message.forward(message.chat.id)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    # insert code here to run it after start


async def on_shutdown(dp):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=False,  # Если True то после восстановления придет только 1 сообщение
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
