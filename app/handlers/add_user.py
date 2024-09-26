import asyncio
from xml.sax.handler import feature_namespaces

from app.loader import dp

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.States import Form
from app.dbtest import db_usercreate

from database import async_session, insert_objects, select_objects

@dp.message(Command("add"))
@dp.message(F.text == "Добввляем пользователя")
async def get_user_name(message: types.Message, state: FSMContext):
    print("step-1")

    await state.set_state(Form.add_user_name)
    await message.answer("Введите имя:")


@dp.message(Form.add_user_name)
async def get_user_info(message: types.Message, state: FSMContext):
    print("step-2")
    await state.update_data(name=message.text)

    await state.set_state(Form.add_user_info)
    await message.answer("Введите фамилию")


@dp.message(Form.add_user_info)
async def get_user_info(message: types.Message, state: FSMContext):
    print("step-3")
    await state.update_data(surname=message.text)

    data = await state.get_data()
    name=data.get("name")
    surname=data.get("surname")

    await insert_objects(async_session, name=name, surname=surname)

    res = await select_objects(async_session)

    await message.answer(res)

    await state.clear()

    print(res)
