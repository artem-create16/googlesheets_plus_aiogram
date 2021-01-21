from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from loader import get_sheet_values
from handlers.users.set_settings import answer_time_for_send


@dp.message_handler(Command('get'))
async def get_message(message: types.Message,
                      state: FSMContext):
    count = (await state.get_data()).get('count')
    chat_id = message.chat.id
    text = get_sheet_values(f'C1:D{count}')
    await bot.send_message(chat_id=chat_id, text=text)

    print(count)
