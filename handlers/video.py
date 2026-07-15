from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from config import ADMIN_ID, ANNOUNCE_CHANNEL, VIP_GROUP

router = Router()

waiting_youtube = set()
waiting_instagram = set()


@router.callback_query(F.data == "youtube")
async def youtube_button(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return

    waiting_youtube.add(callback.from_user.id)

    await callback.message.answer(
        "🎥 YouTube video linkini gönder."
    )

    await callback.answer()


@router.callback_query(F.data == "instagram")
async def instagram_button(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        return

    waiting_instagram.add(callback.from_user.id)

    await callback.message.answer(
        "📸 Instagram Reel/Post linkini gönder."
    )

    await callback.answer()


@router.message()
async def links(message: Message):

    if message.from_user.id in waiting_youtube:

        waiting_youtube.remove(message.from_user.id)

        text = (
            "🎥 <b>Yeni YouTube Videomuz Yayında!</b>\n\n"
            "🔥 Yeni analiz videomuzu kaçırmayın.\n\n"
            f"{message.text}\n\n"
            "🍀 İyi seyirler."
        )

        await message.bot.send_message(
            ANNOUNCE_CHANNEL,
            text,
            parse_mode="HTML"
        )

        await message.bot.send_message(
            VIP_GROUP,
            text,
            parse_mode="HTML"
        )

        await message.answer("✅ YouTube paylaşımı yapıldı.")

        return


    if message.from_user.id in waiting_instagram:

        waiting_instagram.remove(message.from_user.id)

        text = (
            "📸 <b>Yeni Instagram Paylaşımı!</b>\n\n"
            "🔥 Yeni Reel yayında.\n\n"
            f"{message.text}\n\n"
            "❤️ Takip etmeyi unutmayın."
        )

        await message.bot.send_message(
            ANNOUNCE_CHANNEL,
            text,
            parse_mode="HTML"
        )

        await message.bot.send_message(
            VIP_GROUP,
            text,
            parse_mode="HTML"
        )

        await message.answer("✅ Instagram paylaşımı yapıldı.")