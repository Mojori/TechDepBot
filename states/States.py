from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    add_user_info = State()
    add_user_name = State()
