from aiogram import Dispatcher, Bot, Router
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

hello_form_router = Router()

dp.include_router(hello_form_router)
