from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
    
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберие пункт меню.')
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
