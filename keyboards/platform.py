from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PLATFORM_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🤖 ANALİZ BOTU",
                url="https://t.me/RuletDenizBot"
            )
        ],
        [
            InlineKeyboardButton(
                text="💬 SOHBET KANALI",
                url="https://t.me/RuletDenizPrivate"
            ),
            InlineKeyboardButton(
                text="🛡️ YEDEK SOHBET",
                url="https://t.me/ruletdenizvip"
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 ANA SPONSORLAR",
                url="https://ruletdeniz.com/"
            )
        ],
        [
            InlineKeyboardButton(
                text="▶️ YOUTUBE",
                url="https://youtube.com/@ruletdeniz"
            )
        ]
    ]
)