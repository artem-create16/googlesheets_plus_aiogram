from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from loader import get_sheet_values


@dp.message_handler(Command('get'))
async def get_message(message: types.Message, state: FSMContext):
    
    count = (await state.get_data()).get('count')
    text = get_sheet_values(f'C1:D{count}')
    await message.answer(text=text)
