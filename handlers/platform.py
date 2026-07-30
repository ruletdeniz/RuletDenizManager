from aiogram import F

@router.message(F.photo)
async def get_photo_id(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        f"📸 Yeni PHOTO_ID:\n\n<code>{message.photo[-1].file_id}</code>",
        parse_mode="HTML"
    )
    from aiogram import F
from aiogram.types import Message

@router.message(F.photo)
async def get_photo_id(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        f"📸 Yeni PHOTO_ID:\n\n<code>{message.photo[-1].file_id}</code>",
        parse_mode="HTML"
    )