from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
    
],
                           resize_kyeboard=True,
                           input_field_placeholder='Выберие пункт меню.')