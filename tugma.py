from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup,\
    KeyboardButton, ReplyKeyboardMarkup

asosiy_menu = ReplyKeyboardMarkup(
     keyboard = [
    [
       KeyboardButton(text="Ayollar"),
       KeyboardButton(text="Erkakalar"),
       KeyboardButton(text="Qizbolalar")
    ],
    [
       KeyboardButton(text="Oyoq kiyimlar"),
       #KeyboardButton(text="bosh kiyim")

    ],
      [
      # KeyboardButton(text="telifon raqamim")
    ]
  ], resize_keyboard=True
)


Ayollar_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Koylklar",callback_data="ayol_koylak"),
            InlineKeyboardButton(text="Sharflar", callback_data="ayol_sharf"),
        ],
        [
            InlineKeyboardButton(text="Shimlar", callback_data="ayol_shim"),
            InlineKeyboardButton(text="Koftalar", callback_data="ayol_kofta"),
        ],
        [
            InlineKeyboardButton(text="Paltolar", callback_data="ayol_palto"),
            InlineKeyboardButton(text="Kurtkalar", callback_data="ayol_kurtka"),
        ]
    ]
)
erkaklar_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kuylaklar",callback_data="erkak_koelak"),
            InlineKeyboardButton(text="Yahtaklar", callback_data="erkak_yahtak"),
        ],
        [
            InlineKeyboardButton(text="Shimlar", callback_data="erkak_shim"),
            InlineKeyboardButton(text="Futbolkalar", callback_data="erkak_futbolka"),
        ],
        [
            InlineKeyboardButton(text="Paltolar", callback_data="erkak_palto"),
            InlineKeyboardButton(text="Kurtkalar", callback_data="erkak_kurtka"),
        ]
    ]
)
qizbolalar_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kuylaklar",callback_data="qizbola_koelak"),
            InlineKeyboardButton(text="Yupklar", callback_data="qizbola_yupka"),
        ],
        [
            InlineKeyboardButton(text="Shimlar", callback_data="qizbola_shim"),
            InlineKeyboardButton(text="Koftalar", callback_data="qizbola_kofta"),
        ],
        [
            InlineKeyboardButton(text="Paltolar", callback_data="qizbola_palto"),
            InlineKeyboardButton(text="Kurtkalar", callback_data="qizbola_kurtka"),
        ]
    ]
)
Poyafzal_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tuflilar",callback_data="tufli"),
            InlineKeyboardButton(text="Sandallar", callback_data="sandal"),
        ],
        [
            InlineKeyboardButton(text="Tapochkalar", callback_data="tapochka"),
            InlineKeyboardButton(text="Slanslar", callback_data="slans"),
        ],
        [
            InlineKeyboardButton(text="Etiklar", callback_data="etik"),
            InlineKeyboardButton(text="Kalishlar", callback_data="kalish"),
        ]
    ]
)















