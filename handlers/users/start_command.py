import sqlite3

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, db


@dp.message_handler(Command('start'))
@dp.throttled(rate=2)
async def start(message: types.Message):
    try:
        db.add_user(user_id=message.from_user.id,)
    except sqlite3.IntegrityError as err:
        print(err)
    await message.answer(f'Hi, {message.from_user.full_name}, my commands: /settings, /next')
