
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton(text='/start'),
    KeyboardButton(text='/info'),
    KeyboardButton(text='/add_product'),
    KeyboardButton(text='/products'),
    KeyboardButton(text='/order'),
)

cancel = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton("Cancel"),
)

submit = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4).add(
    KeyboardButton("Submit"),
    KeyboardButton("Cancel"),
)