# Inline Keyboard + FSM kombinatsiyasi
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

class Survey(StatesGroup):
    q1 = State()
    q2 = State()

@dp.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Ha ✅", callback_data="yes")],
        [InlineKeyboardButton(text="Yo‘q ❌", callback_data="no")]
    ])
    await message.answer("Aiogram sizga yoqdimi?", reply_markup=ikb)
    await state.set_state(Survey.q1)

@dp.callback_query(Survey.q1)
async def answer_q1(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(q1=callback.data)
    await callback.message.answer("Qaysi versiyada ishlayapsiz?")
    await state.set_state(Survey.q2)
    await callback.answer()

@dp.message(Survey.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f"✅ So‘rovnoma tugadi:\n"
                         f"1-savol: {data['q1']}\n"
                         f"2-savol: {message.text}")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

