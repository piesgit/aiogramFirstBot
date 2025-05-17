import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')

async def main():
    logging.basicConfig(level=logging.INFO)  # Исправлено levels -> level
    await dp.start_polling(bot)

if __name__ == '__main__':  # Исправлено name -> name и добавлены кавычки
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
