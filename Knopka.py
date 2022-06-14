from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup,CallbackQuery

Shaharlar = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Shaharlar"),
            KeyboardButton(text="Shahar nomini kiriting"),
        ],
    ],resize_keyboard=True
)
Shaharlar1=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Toshkent",callback_data="Toshkent"),
            InlineKeyboardButton(text="Buxoro",callback_data="Bukhara"),
        ],
        [
            InlineKeyboardButton(text="Samarqand",callback_data="Samarkhand"),
            InlineKeyboardButton(text="Andijon",callback_data="Andijan"),
        ],
        [
            InlineKeyboardButton(text="Navoiy",callback_data="Navoiy"),
            InlineKeyboardButton(text="Namangan",callback_data="Namangan"),
        ],
        [
            InlineKeyboardButton(text="Fargona",callback_data="Fergana"),
            InlineKeyboardButton(text="Sirdaryo",callback_data="Sirdarya"),
        ],
        [
            InlineKeyboardButton(text="Xorazm",callback_data="Khorazem"),
            InlineKeyboardButton(text="Qashqadaryo",callback_data="Kashkadaryo"),
        ],
        [
            InlineKeyboardButton(text="Surxandaryo",callback_data="Surkhandaryo"),
            InlineKeyboardButton(text="Qoraqalpogiston",callback_data="Korakalpogiston"),
        ],
    ]
)