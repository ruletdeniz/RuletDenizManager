from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID, ANNOUNCE_CHANNEL, VIP_GROUP

router = Router()

waiting = set()


@router.message(Command("duyuru"))
async def duyuru(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    waiting.add(message.from_user.id)

    await message.answer("📢 Göndermek istediğin duyuruyu yaz.")


@router.message()
async def send_announce(message: Message):

    # Beklemiyorsa hiçbir şey yapma
    if message.from_user.id not in waiting:
        return

    # Komut geldiyse çık
    if message.text and message.text.startswith("/"):
        return

    waiting.remove(message.from_user.id)

    await message.bot.send_message(
        ANNOUNCE_CHANNEL,
        message.text
    )

    await message.bot.send_message(
        VIP_GROUP,
        message.text
    )

    await message.answer("✅ Duyuru başarıyla paylaşıldı.")