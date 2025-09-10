import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "YOUR_BOT_TOKEN"
dp = Dispatcher()

# 1) Oddiy /start
@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Salom! Bu /start komandasi.")

# 2) Bir nechta komandalar
@dp.message(Command(commands=["hello", "lang"]))
async def multi_cmd(message: Message):
    await message.answer("Siz /hello yoki /lang komandalaridan birini yubordingiz.")

# 3) /help komandasi
@dp.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("Men sizga yordam bera olaman.\n"
                         "Komandalar:\n"
                         "/start\n"
                         "/hello\n"
                         "/lang\n"
                         "/help")

# 4) Echo handler
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
