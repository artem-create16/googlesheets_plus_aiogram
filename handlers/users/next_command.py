from loader import dp, db

from aiogram import types
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('next'))
async def next_step(message: types.Message):
    print(db.select_current_settings(user_id=message.from_user.id))
