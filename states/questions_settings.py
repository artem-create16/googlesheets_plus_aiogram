from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    count_words = State()
    time_for_send = State()
