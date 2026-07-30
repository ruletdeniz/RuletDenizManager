from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID, ANNOUNCE_CHANNEL, VIP_GROUP
from keyboards.platform import PLATFORM_BUTTONS

router = Router()

PHOTO_ID = "AgACAgQAAxkBAAMUaleijIri2VAbNgUzT6TlDEN3UewAAm8NaxtVBsFSEpo-jsSPwm0BAAMCAAN5AAM9BA"


@router.message(Command("platform"))
async def platform(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    # Duyuru Kanalı
    await message.bot.send_photo(
        chat_id=ANNOUNCE_CHANNEL,
        photo=PHOTO_ID,
        reply_markup=PLATFORM_BUTTONS
    )

    # VIP Lounge
    await message.bot.send_photo(
        chat_id=VIP_GROUP,
        photo=PHOTO_ID,
        reply_markup=PLATFORM_BUTTONS
    )

    await message.answer("✅ Platform paylaşımı başarıyla yapıldı.")