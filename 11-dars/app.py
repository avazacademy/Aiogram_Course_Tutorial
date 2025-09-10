from aiogram import Bot, Dispatcher, types, BaseMiddleware
 
from aiogram.filters import Command
from typing import Callable, Awaitable, Dict, Any
import asyncio
import logging
import time

TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔹 Antiflood Middleware
class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, limit_time: int = 3):
        super().__init__()
        self.limit_time = limit_time
        self.last_message_time: Dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        now = time.time()

        # agar foydalanuvchi ilgari yozgan bo‘lsa
        if user_id in self.last_message_time:
            diff = now - self.last_message_time[user_id]
            if diff < self.limit_time:  # tez-tez yozsa bloklaymiz
                await event.answer("⛔ Juda tez yozayapsiz, biroz kuting!")
                return

        # oxirgi yozgan vaqtini saqlash
        self.last_message_time[user_id] = now

        # Handlerga o‘tkazamiz
        return await handler(event, data)

# Middleware qo‘shamiz
dp.message.middleware(AntiFloodMiddleware(limit_time=3))

# 🔹 Oddiy handlerlar
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom 👋\nBu botda antiflood ishlatilmoqda.\nXabar yuboring.")

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# 🔹 Botni ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
