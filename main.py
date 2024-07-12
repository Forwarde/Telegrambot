import asyncio
from aiogram import Dispatcher, Bot

from app.handler import router

async def main():
    bot = Bot(token='6900975068:AAGl5POfN9XTLHXDvNw8MjjXm_PWO2LfZ9Y')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Бот включен")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
