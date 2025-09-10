import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
 
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from database import create_db, add_class, get_classes, add_student, get_students_by_class

TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# 🔹 FSM holatlari
class StudentRegister(StatesGroup):
    class_id = State()
    first_name = State()
    last_name = State()

# 🔹 Start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    kb = ReplyKeyboardBuilder()
    kb.button(text="🏫 Sinf qo‘shish")
    kb.button(text="👨‍🎓 Talaba qo‘shish")
    kb.button(text="📋 Talabalar ro‘yxati")
    kb.adjust(1)

    await message.answer("👋 Xush kelibsiz! Amallardan birini tanlang:", 
                         reply_markup=kb.as_markup(resize_keyboard=True))

# 🔹 Sinf qo‘shish
@dp.message(F.text == "🏫 Sinf qo‘shish")
async def add_class_handler(message: types.Message):
    await message.answer("✏️ Yangi sinf nomini kiriting (masalan: 7-A):")

@dp.message(F.text.regexp(r"^\d{1,2}-[A-Z]$"))
async def process_class_name(message: types.Message):
    add_class(message.text)
    await message.answer(f"✅ Sinf qo‘shildi: {message.text}")

# 🔹 Talaba qo‘shish
@dp.message(F.text == "👨‍🎓 Talaba qo‘shish")
async def add_student_start(message: types.Message, state: FSMContext):
    classes = get_classes()
    if not classes:
        await message.answer("❌ Hali sinflar yo‘q. Avval sinf qo‘shing.")
        return
    
    kb = InlineKeyboardBuilder()
    for cid, cname in classes:
        kb.button(text=cname, callback_data=f"class_{cid}")
    kb.adjust(2)

    await message.answer("📚 Qaysi sinfga talaba qo‘shamiz?", reply_markup=kb.as_markup())
    await state.set_state(StudentRegister.class_id)

@dp.callback_query(StudentRegister.class_id, F.data.startswith("class_"))
async def process_class(callback: types.CallbackQuery, state: FSMContext):
    class_id = int(callback.data.split("_")[1])
    await state.update_data(class_id=class_id)

    await callback.message.answer("✏️ Talabaning ismini kiriting:")
    await state.set_state(StudentRegister.first_name)
    await callback.answer()

@dp.message(StudentRegister.first_name)
async def process_first_name(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer("✏️ Endi familiyasini kiriting:")
    await state.set_state(StudentRegister.last_name)

@dp.message(StudentRegister.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    class_id = data["class_id"]
    first_name = data["first_name"]
    last_name = message.text

    add_student(class_id, first_name, last_name)

    await message.answer(f"✅ Talaba qo‘shildi:\n{first_name} {last_name}")
    await state.clear()

# 🔹 Ro‘yxat
@dp.message(F.text == "📋 Talabalar ro‘yxati")
async def show_students(message: types.Message):
    classes = get_classes()
    if not classes:
        await message.answer("❌ Sinflar mavjud emas.")
        return
    
    kb = InlineKeyboardBuilder()
    for cid, cname in classes:
        kb.button(text=cname, callback_data=f"show_{cid}")
    kb.adjust(2)

    await message.answer("📌 Qaysi sinf ro‘yxatini ko‘rmoqchisiz?", reply_markup=kb.as_markup())

@dp.callback_query(F.data.startswith("show_"))
async def show_class_students(callback: types.CallbackQuery):
    class_id = int(callback.data.split("_")[1])
    students = get_students_by_class(class_id)

    if not students:
        text = "❌ Bu sinfda talabalar yo‘q."
    else:
        text = "👥 Talabalar ro‘yxati:\n\n"
        for i, (fname, lname) in enumerate(students, start=1):
            text += f"{i}. {fname} {lname}\n"

    await callback.message.answer(text)
    await callback.answer()

# 🔹 Run bot
async def main():
    logging.basicConfig(level=logging.INFO)
    create_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
