# bot.py

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio
import logging

# 🔑 Tokenni shu yerga yozing
TOKEN = "1234567890:ABCDEFghIjklMNopQrstUVwxyz"

# Bot va dispatcher
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start komandasi
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Default tugmalar (reply buttons)
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Kurslar"), KeyboardButton(text="ℹ️ Biz haqimizda")],
            [KeyboardButton(text="🌐 Websayt")],
        ],
        resize_keyboard=True,   # tugmalar ekran o‘lchamiga mos bo‘ladi
        one_time_keyboard=False # tugma bosilgandan keyin ham yo‘qolmaydi
    )

    await message.answer("Salom 👋\nQuyidagilardan birini tanlang:", reply_markup=keyboard)


# Tugmalarga javob qaytarish
@dp.message()
async def reply_handler(message: types.Message):
    if message.text == "📚 Kurslar":
        await message.answer("📚 Bizda mavjud kurslar:\n- Python\n- Telegram Bot\n- HTML/CSS")
    elif message.text == "ℹ️ Biz haqimizda":
        await message.answer("ℹ️ Bu bot test uchun yaratilgan.\nAdmin: @username")
    elif message.text == "🌐 Websayt":
        await message.answer("🌐 Websayt: https://google.com")
    else:
        await message.answer("❓ Menusdan tanlang.")


# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
