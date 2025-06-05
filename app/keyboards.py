from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
    InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com')]
    ])

cars = ['Tesla', 'Mercedes', 'BMW', 'Porshe']

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
        # 14:55, тут нельзя только текст, можно url и т. д.
    return keyboard.adjust(2).as_markup() # урок 4, 14:40, adjust(2-3-4-5...), .as_markup() ОБЯЗАТЕЛЬНО
