import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

dp = Dispatcher()
bot = Bot(token=TOKEN)

# /menu komandasi tugmalarni chiqaradi
@dp.message(Command("menu"))
async def show_menu(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[
            # Oddiy matn tugmalari
            [KeyboardButton(text="🍔 Burger"), KeyboardButton(text="🍕 Pizza")],

            # Telefon raqam so‘rash tugmasi
            [KeyboardButton(text="📱 Telefon raqamimni yuborish", request_contact=True)],

            # Joylashuv so‘rash tugmasi
            [KeyboardButton(text="📍 Joylashuvimni yuborish", request_location=True)]
        ],

        # 📌 resize_keyboard=True → tugmalar ekran o‘lchamiga moslashadi (kichkina bo‘ladi)
        resize_keyboard=True,

        # 📌 one_time_keyboard=True → foydalanuvchi tugma bosgandan keyin klaviatura yo‘qoladi
        one_time_keyboard=True,

        # 📌 input_field_placeholder="..." → yozish joyida ko‘rinadigan yordamchi matn
        input_field_placeholder="Iltimos, menyudan tanlang...",

        # 📌 selective=False → klaviatura hamma uchun ko‘rinadi
        selective=False,

        # 📌 is_persistent=True → tugmalar doimiy bo‘lib qoladi, bot boshqa xabar yuborsa ham yo‘qolmaydi
        is_persistent=True
    )

    await message.answer("Menyudan biror narsani tanlang 👇", reply_markup=kb)


# Echo handler → foydalanuvchi tanlagan narsani qaytaradi
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Siz tanladingiz: {message.text}")


# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
