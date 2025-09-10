from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
import logging

TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1️⃣ Holatlar klassi
class RegisterForm(StatesGroup):
    name = State()
    age = State()
    phone = State()

# /start -> ro‘yxatni boshlash
@dp.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Salom 👋\nRo‘yxatdan o‘tishni boshlaymiz.\n\nIsmingizni kiriting:")
    await state.set_state(RegisterForm.name)

# 2️⃣ Ismni qabul qilish
@dp.message(RegisterForm.name, F.text)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)  # ismni saqlash
    await message.answer("✅ Ism qabul qilindi.\n\nEndi yoshingizni kiriting:")
    await state.set_state(RegisterForm.age)

# 3️⃣ Yoshni qabul qilish
@dp.message(RegisterForm.age, F.text)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Yosh faqat son bo‘lishi kerak. Qayta kiriting:")
        return
    
    await state.update_data(age=message.text)
    await message.answer("✅ Yosh qabul qilindi.\n\nTelefon raqamingizni yuboring:")
    await state.set_state(RegisterForm.phone)

# 4️⃣ Telefon raqamni qabul qilish
@dp.message(RegisterForm.phone, F.text)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)

    # barcha ma'lumotlarni olish
    data = await state.get_data()
    name = data["name"]
    age = data["age"]
    phone = data["phone"]

    await message.answer(
        f"📋 Ro‘yxatdan o‘tish tugadi!\n\n"
        f"👤 Ism: {name}\n"
        f"🔢 Yosh: {age}\n"
        f"📞 Telefon: {phone}"
    )

    # Holatni tugatish
    await state.clear()

# 5️⃣ /cancel komandasi – ro‘yxatni to‘xtatish
@dp.message(Command("cancel"))
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("❌ Ro‘yxatdan o‘tish bekor qilindi.")

# Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
