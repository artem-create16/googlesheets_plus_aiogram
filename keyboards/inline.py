from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/next"),
        ]
    ],
    resize_keyboard=True
)
