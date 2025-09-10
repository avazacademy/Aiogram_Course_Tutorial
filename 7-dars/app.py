# bot.py

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
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
    # Inline tugmalar
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 Kurslar", callback_data="kurslar"),
                InlineKeyboardButton(text="ℹ️ Biz haqimizda", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="🌐 Websayt", url="https://google.com")
            ]
        ]
    )

    await message.answer("Salom 👋\nQuyidagilardan birini tanlang:", reply_markup=keyboard)


# callback_query hodisasi
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "kurslar":
        await callback.message.answer("📚 Bizda mavjud kurslar:\n- Python\n- Telegram Bot\n- HTML/CSS")
    elif callback.data == "about":
        await callback.message.answer("ℹ️ Bu bot test uchun yaratilgan.\nAdmin: @username")

    # 👉 bu qator shart, tugmani bosganda “loading” belgisi yo‘qolishi uchun
    await callback.answer()


# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
