from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PLATFORM_BUTTONS = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🤖 Analiz Botu",
                url="https://t.me/RuletDenizBot"
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 VIP Lounge",
                url="https://t.me/RuletDenizPrivate"
            ),
            InlineKeyboardButton(
                text="📸 Instagram",
                url="https://www.instagram.com/ruletdeniz"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎥 YouTube",
                url="https://www.youtube.com/@RuletDeniz"
            ),
            InlineKeyboardButton(
                text="🎬 Yedek Kanal",
                url="https://www.youtube.com/@RuletDenizYedek"
            )
        ],
        [
            InlineKeyboardButton(
                text="🌐 Sponsorlar",
                url="https://heylink.me/ruletdeniz"
            ),
            InlineKeyboardButton(
                text="👤 Moderatör",
                url="https://t.me/RdenizDestek"
            )
        ]
    ]
)