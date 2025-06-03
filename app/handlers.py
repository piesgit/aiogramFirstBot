from aiogram import F, Router # Импорт F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет!\nВот твой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}',
                        reply_markup=await kb.inline_cars()) # Получение и вывод ID пользователя

    
@router.message(Command("help"))
async def get_help(message: Message):
    await message.answer('Это команда /help')
    
# F текст
    
@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('ОК!')
    
# Отправка фото по ID
    
@router.message(Command('get_photo_by_id'))
async def get_photo_by_id(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAANNaCi9865mpHeT0DwMz9aMWr6CmiUAAqL3MRvxokhJXKeM78OvoSkBAAMCAAN5AAM2BA',
                               caption='Это НЕ лого ТГ')
    
# Отправка фото по ссылке

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://img.freepik.com/free-photo/beautiful-shot-of-a-white-british-shorthair-kitten_181624-57681.jpg',
                               caption='Это фото с Интернета')
 
# F фото
    
@router.message(F.photo)
async def handle_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')