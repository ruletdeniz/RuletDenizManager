from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PANEL = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Duyuru",
                callback_data="announce"
            ),
            InlineKeyboardButton(
                text="🖼 Platform",
                callback_data="platform"
            )
        ],
        [
            InlineKeyboardButton(
                text="📸 Instagram",
                callback_data="instagram"
            ),
            InlineKeyboardButton(
                text="🎥 YouTube",
                callback_data="youtube"
            )
        ],
        [
            InlineKeyboardButton(
                text="📷 Fotoğraf",
                callback_data="photo"
            ),
            InlineKeyboardButton(
                text="🌐 Sponsorlar",
                callback_data="sponsors"
            )
        ],
        [
            InlineKeyboardButton(
                text="📊 Anket",
                callback_data="poll"
            ),
            InlineKeyboardButton(
                text="📌 Sabitle",
                callback_data="pin"
            )
        ],
        [
            InlineKeyboardButton(
                text="🗑 Sil",
                callback_data="delete"
            ),
            InlineKeyboardButton(
                text="⚙ Ayarlar",
                callback_data="settings"
            )
        ]
    ]
)