from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser
change_language_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Uzbekcha🇺🇿"),
            KeyboardButton(text="Русский🇷🇺")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

phone_number_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить номер телефона📞", request_contact=True)
        ],
    ],
    resize_keyboard=True
)

lokatsion_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить местоположение📍", request_location=True)
        ],
    ],
    resize_keyboard=True
)

menu_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Услуги 💼"),
        ],
        [
            KeyboardButton("Предложения и жалобы ✍️"),
            KeyboardButton("Социальные сети 🌐")
        ],
        [
            KeyboardButton("Настройки ⚙️")
        ]
    ],
    resize_keyboard=True
)

xizmatlar_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Генеральная уборка 🛠"),
            KeyboardButton("Влажная уборка 💧")
        ],
        [
            KeyboardButton("Генеральная уборка с робоклином 🤖")
        ],
        [
            KeyboardButton("Дополнительные услуги ➕")
        ],
        [
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

jamixizmatlar_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("обеспыливание и чистка полов"),
            KeyboardButton("Обеспыливание ковров ")
        ],
        [
            KeyboardButton("Обеспыливание и чистка люстр"),
            KeyboardButton("Обеспыливание  и чистка потолков")
        ],
        [
            KeyboardButton("Обеспыливание и чистка обои"),
            KeyboardButton("Чистка ванн")
        ],
        [
            KeyboardButton("чистка туалета. (Сан.узлов)"),
            KeyboardButton("Чистка оконных блогов и стёкол")
        ],
        [
            KeyboardButton("Чистка мебели"),
        ],
        [
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

nam_xizmatlar_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("обеспыливание и чистка полов"),
            KeyboardButton("Обеспыливание ковров")
        ],
        [
            KeyboardButton("Чистка ванн"),
            KeyboardButton("чистка туалета. (Сан.узлов)")
        ],
        [
            KeyboardButton("Чистка оконных блогов и стёкол")
        ],
        [
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

Roboclean_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("обеспыливание и чистка полов"),
            KeyboardButton("Обеспыливание ковров")
        ],
        [
            KeyboardButton("Обеспыливание и чистка люстр"),
            KeyboardButton("Обеспыливание  и чистка потолков")
        ],
        [
            KeyboardButton(" Обеспыливание и чистка обои"),
            KeyboardButton("Чистка ванн")
        ],
        [
            KeyboardButton("чистка туалета. (Сан.узлов)"),
            KeyboardButton("Чистка оконных блогов и стёкол")
        ],
        [
            KeyboardButton("Чистка мебели"),
            KeyboardButton("Стирка ковров(на месте с робоклин")
        ],
        [
            KeyboardButton("Химчистка мебел"),
            KeyboardButton("Химчистка матрасов")
        ],
        [
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)


qoshimchaxizmatlar_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("митьё посуд"),
            KeyboardButton("Привести  порядок в гардеробах")
        ],
        [
            KeyboardButton("Уборка в подвалных помещениях "),
            KeyboardButton("Поглаживание")
        ],
        [
            KeyboardButton("Мытья брусчаток"),
            KeyboardButton("Чистка алюкобонд")
        ],
        [
            KeyboardButton("Стрижка газонов (газонокосилка)"),
            KeyboardButton("Мытье и чистка фасад")
        ],
        [
            KeyboardButton("Дезинфекция "),
            KeyboardButton("Митьё и поглаживание штор")
        ],
        [
            KeyboardButton("Назад 🔙")
        ],
    ],
    resize_keyboard=True
)

settings_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Изменить номер телефона 📞"),
            KeyboardButton("Изменить ФИО 👤")
        ],
        [
            KeyboardButton("Удалить профиль 🗑"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

admin_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Статистика 📊 "),
            KeyboardButton(text="Пользователи 👥")
        ],
    ],
    resize_keyboard=True
)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

savat_btn_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить заказ✅", callback_data="tas"),
            InlineKeyboardButton(text="Отклонить заказы❌", callback_data="rad")
        ]
    ],
)