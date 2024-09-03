from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser

change_language = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbekcha🇺🇿"),
            KeyboardButton(text="Русский🇷🇺")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

phone_number_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqam jonatish📞", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

lokatsion = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lokatsiya yuboring📍", request_location=True)
        ],
    ],
    resize_keyboard=True
)

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Xizmatlar 💼"),
        ],
        [
            KeyboardButton("Taklif Shikoyatlar ✍️"),
            KeyboardButton("Ijtimoiy Tarmoqlar 🌐")
        ],
        [
            KeyboardButton("Sozlamalar ⚙️")
        ]
    ],
    resize_keyboard=True
)

xizmatlar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Генеральная уборка  🛠"),
            KeyboardButton("Влажная уборка  💧")
        ],
        [

            KeyboardButton("Генеральная уборка с робоклином  🤖")
        ],
        [
            KeyboardButton("Qo'shimcha xizmatlar ➕")
        ],
        [
            KeyboardButton("Orqaga 🔙")
        ]
    ],
    resize_keyboard=True
)
list1 = ["Hamma changini olish","Gilamni changini olish","Oboy changini olish","Qandillarning changini olish","Shift changini olish",

"Hammom tozalash",
"Tualet tozalash",
"Oynalarni tozalash",
"Mebellarni changini olish"
         ]
jamixizmatlar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Polni changini olish"),
            KeyboardButton("Gilamni changini olish")
        ],
        [
            KeyboardButton("Oboy changini olish"),
            KeyboardButton("Qandillarning changini olish")
        ],
        [
            KeyboardButton("Shift changini olish"),
            KeyboardButton("Hammom tozalash")
        ],
        [
            KeyboardButton("Tualet tozalash"),
            KeyboardButton("Oynalarni tozalash")
        ],
        [
            KeyboardButton("Mebellarni changini olish"),
        ],
        [
            KeyboardButton("Orqaga 🔙")
        ]
    ],
    resize_keyboard=True
)

nam_xizmatlar_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Polni changini olish"),
            KeyboardButton("Gilamni changini olish")
        ],
        [
            KeyboardButton("Sanuzel tozalash"),
            KeyboardButton("Oynalarni tozalash")
        ],
        [
            KeyboardButton("Mebellarni changini olish")
        ],
        [
            KeyboardButton("Orqaga 🔙")
        ]
    ],
    resize_keyboard=True
)

Roboclean_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Polni changini olish"),
            KeyboardButton("Gilamni changini olish")
        ],
        [
            KeyboardButton("Oboy changini olish"),
            KeyboardButton("Qandillarning changini olish")
        ],
        [
            KeyboardButton("Shift changini olish"),
            KeyboardButton("Hammom tozalash")
        ],
        [
            KeyboardButton("Tualet tozalash"),
            KeyboardButton("Oynalarni tozalash")
        ],
        [
            KeyboardButton("Mebellarni changini olish"),
            KeyboardButton("Gilamlarni joyida yuvish")
        ],
        [
            KeyboardButton("Divan ximchistka"),
            KeyboardButton("Matras ximchistka")
        ],
        [
            KeyboardButton("Orqaga 🔙")
        ]
    ],
    resize_keyboard=True
)


qoshimchaxizmatlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Idishlarni yuvish"),
            KeyboardButton("Kiyimlarni tartibga keltirish")
        ],
        [
            KeyboardButton("Padvalni tartibga keltirish"),
            KeyboardButton("Buyumlarni tartibga keltirish")
        ],
        [
            KeyboardButton("Kiyimlarni dazmollash"),
            KeyboardButton("Bruschatka tozalash")
        ],
        [
            KeyboardButton("Alikafon tozalash"),
            KeyboardButton("Gazonakosilka")
        ],
        [
            KeyboardButton("Fasad yuvish"),
            KeyboardButton("Dezinfeksiya")
        ],
        [
            KeyboardButton("Pardalarni yuvib dazmollash"),
            KeyboardButton("Orqaga 🔙")
        ],
    ],
    resize_keyboard=True
)

settings_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Telefon Nomerni O'zgartirish 📞"),
            KeyboardButton("Ism Familyani O'zgartirish 👤")
        ],
        [
            KeyboardButton("Profilni O'chirish 🗑"),
            KeyboardButton("Orqaga 🔙")
        ]
    ],
    resize_keyboard=True
)

admin_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Statistika 📊 "),
            KeyboardButton(text="Foydalanuvchilar 👥")
        ],
    ],
    resize_keyboard=True
)



from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

savat_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zakazni tasdiqlash✅", callback_data="tasdiqlash"),
            InlineKeyboardButton(text="Zakazlarni rad etish❌", callback_data="radetish")
        ]
    ],
)