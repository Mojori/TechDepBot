import asyncio
from aiogram.types import BotCommand
from app.loader import dp, bot
from app import handlers
from database import async_main


async def main() -> None:
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Старт"),
            BotCommand(command="/add", description="Добвать пользователя"),
        ]
    )

    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())
