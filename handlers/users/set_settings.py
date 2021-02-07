from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states.questions_settings import Form
from loader import db


@dp.message_handler(Command('settings'))
async def enter_to_settings(message: types.Message):
    await message.answer('Give me count of words')

    await Form.count_words.set()


@dp.message_handler(state=Form.count_words)
async def answer_count_of_words(message: types.Message,
                                state: FSMContext):
    count_words = message.text
    await state.update_data(count=count_words)

    await message.answer('Nice! Now give me time')
    await Form.next()


@dp.message_handler(state=Form.time_for_send)
async def answer_time_for_send(message: types.Message,
                               state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    count = data.get("count")
    db.update_settings(start_point=1, count_of_words=count, end_point=count,
                       time=message.text, user_id=message.from_user.id)

    await message.answer(f'Your answers: '
                         f'count - {count}, time - {message.text}')
    print(db.select_all_users())
    await state.reset_state(with_data=False)
    return data
