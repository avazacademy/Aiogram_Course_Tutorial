# bot.py

from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
 
from aiogram.filters import Command
import asyncio
import logging

# 🔑 Tokenni shu yerga yozing
TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

# Bot va dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start komandasi
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Inline tugmalar
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 Kurslar", url="https://google.com"),
                InlineKeyboardButton(text="ℹ️ Biz haqimizda", url="https://t.me/username"),
            ]
        ]
    )
    await message.answer("Salom 👋\nQuyidagilardan birini tanlang:", reply_markup=keyboard)


# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
