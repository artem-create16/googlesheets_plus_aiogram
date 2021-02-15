from aiogram.dispatcher.filters import Command

from keyboards.inline import button
from loader import dp, db
from loader import get_sheet_values


@dp.message_handler(Command('next'))
@dp.throttled(rate=2)
async def get_message(message):
    value = db.select_user(user_id=message.from_user.id)
    count, start, end = value[1], value[2], value[3]
    text = get_sheet_values(f'C{start}:D{end}')
    await message.answer(text=text, reply_markup=button)
    db.update_value_for_next_command(start_point=start+count,
                                     end_point=end+count,
                                     user_id=message.from_user.id)

    print(db.select_all_users())
#
# @dp.callback_query_handler(callback.filter(button_name='next_command'))
# async def get_message(message: types.Message):
#     await message.answer(text='+')