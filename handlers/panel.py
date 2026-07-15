from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import ADMIN_ID
from keyboards.panel import PANEL

router = Router()


@router.message(Command("panel"))
async def panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    await message.answer(
        "👑 <b>Rulet Deniz Manager Paneli</b>\n\n"
        "Yapmak istediğin işlemi seç.",
        parse_mode="HTML",
        reply_markup=PANEL
    )


@router.callback_query(F.data == "platform")
async def platform_button(callback: CallbackQuery):

    if callback.from_user.id != ADMIN_ID:
        await callback.answer()
        return

    await callback.message.answer("✅ Platform butonuna basıldı.")

    await callback.answer()