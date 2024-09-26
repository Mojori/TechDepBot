from app.loader import dp
from aiogram.filters import Command
from aiogram import types


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет, ку, здарова, мяу")
