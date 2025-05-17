import asyncio
import logging

from aiogram import Bot, Dispatcher, F # Импорт F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    
@dp.message(Command("help"))
async def get_help(message: Message):
    await message.answer('Это команда /help')
    
# F текст
    
@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК!')
    
# Отправка фото по ID
    
@dp.message(Command('get_photo_by_id'))
async def get_photo_by_id(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAANNaCi9865mpHeT0DwMz9aMWr6CmiUAAqL3MRvxokhJXKeM78OvoSkBAAMCAAN5AAM2BA',
                               caption='Это НЕ лого ТГ')
    
# Отправка фото по ссылке

# Нужно удалить

@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://img.freepik.com/free-photo/beautiful-shot-of-a-white-british-shorthair-kitten_181624-57681.jpg',
                               caption='Это фото с Интернета')
 
# F фото
    
@dp.message(F.photo)
async def handle_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
