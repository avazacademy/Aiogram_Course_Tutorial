from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
import asyncio
import logging

TOKEN = "1234567890:ABCDEFghIjklMNopQrstUVwxyz"

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Salom 👋\nMenga rasm, video, stiker yoki ovoz yuboring – men aniqlayman.")

# Matn
@dp.message(F.text)
async def detect_text(message: types.Message):
    await message.answer("✉️ Siz matn yubordingiz.")

# Rasm
@dp.message(F.photo)
async def detect_photo(message: types.Message):
    await message.answer("📷 Siz rasm yubordingiz.")

# Video
@dp.message(F.video)
async def detect_video(message: types.Message):
    await message.answer("🎥 Siz video yubordingiz.")

# Ovozli xabar
@dp.message(F.voice)
async def detect_voice(message: types.Message):
    await message.answer("🎙 Siz ovozli xabar yubordingiz.")

# Musiqa
@dp.message(F.audio)
async def detect_audio(message: types.Message):
    await message.answer("🎵 Siz musiqa yubordingiz.")

# Sticker
@dp.message(F.sticker)
async def detect_sticker(message: types.Message):
    await message.answer("😅 Siz sticker yubordingiz.")

# GIF (animation)
@dp.message(F.animation)
async def detect_gif(message: types.Message):
    await message.answer("🎁 Siz GIF yubordingiz.")

# Kontakt
@dp.message(F.contact)
async def detect_contact(message: types.Message):
    await message.answer(f"👤 Siz kontakt yubordingiz:\n{message.contact.first_name} - {message.contact.phone_number}")

# Lokatsiya
@dp.message(F.location)
async def detect_location(message: types.Message):
    await message.answer(f"📍 Siz joylashuv yubordingiz.\nLat: {message.location.latitude}, Lon: {message.location.longitude}")

# Dumaloq video (video note)
@dp.message(F.video_note)
async def detect_video_note(message: types.Message):
    await message.answer("🔗 Siz dumaloq video (video note) yubordingiz.")

# Run
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
