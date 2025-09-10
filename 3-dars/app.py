import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "8356207239:AAGOiH-aBfXPUKj-9Cr4LtZj1hqL0DBqFA0"
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    user = message.from_user

    info = (
        f"🆔 ID: {user.id}\n"
        f"👤 Ism: {user.first_name}\n"
        f"👥 Familiya: {user.last_name if user.last_name else '❌ Kiritilmagan'}\n"
        f"📛 Username: @{user.username if user.username else '❌ Yo‘q'}\n"
        f"⭐ Premium: {'✅ Ha' if user.is_premium else '❌ Yo‘q'}\n"
        f"🌐 Til kodi: {user.language_code}\n"
        f"🤖 Botmi: {'✅ Ha' if user.is_bot else '❌ Yo‘q'}"
    )

    await message.answer("Salom! Siz haqingizdagi ma’lumotlar:\n\n" + info)

 

@dp.message(Command("photo"))
async def get_photo(message: Message, bot: Bot):
    photos = await bot.get_user_profile_photos(message.from_user.id)
    if photos.total_count > 0:
        file_id = photos.photos[0][0].file_id
        await message.answer_photo(file_id, caption="Sizning profil rasmi")
    else:
        await message.answer("Profil rasm topilmadi.")
# Botni ishga tushirish
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
