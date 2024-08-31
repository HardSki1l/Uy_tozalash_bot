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
            KeyboardButton(text="Отправить локацию📍", request_location=True)
        ],
    ],
    resize_keyboard=True
)

menu_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Услуги 💼"),
            KeyboardButton("Корзина 🛒")
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
            KeyboardButton("Все услуги 🛠"),
            KeyboardButton("Мокрая уборка 💧")
        ],
        [
            KeyboardButton("Общая уборка 🏚"),
            KeyboardButton("Уборка RoboClenda 🤖")
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
            KeyboardButton("Сухая уборка"),
            KeyboardButton("Чистка ковра")
        ],
        [
            KeyboardButton("Чистка обоев"),
            KeyboardButton("Чистка люстр")
        ],
        [
            KeyboardButton("Чистка потолка"),
            KeyboardButton("Уборка ванной")
        ],
        [
            KeyboardButton("Уборка туалета"),
            KeyboardButton("Мойка окон")
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
            KeyboardButton("Мойка пола"),
            KeyboardButton("Чистка ковра")
        ],
        [
            KeyboardButton("Уборка санузла"),
            KeyboardButton("Мойка окон")
        ],
        [
            KeyboardButton("Чистка мебели")
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
            KeyboardButton("Мойка пола"),
            KeyboardButton("Чистка ковра")
        ],
        [
            KeyboardButton("Чистка обоев"),
            KeyboardButton("Чистка люстр")
        ],
        [
            KeyboardButton("Чистка потолка"),
            KeyboardButton("Уборка ванной")
        ],
        [
            KeyboardButton("Уборка туалета"),
            KeyboardButton("Мойка окон")
        ],
        [
            KeyboardButton("Чистка мебели"),
            KeyboardButton("Стирка ковров на месте")
        ],
        [
            KeyboardButton("Химчистка дивана"),
            KeyboardButton("Химчистка матраса")
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
            KeyboardButton("Мойка посуды"),
            KeyboardButton("Упорядочение одежды")
        ],
        [
            KeyboardButton("Упорядочение подвала"),
            KeyboardButton("Упорядочение вещей")
        ],
        [
            KeyboardButton("Глажка одежды"),
            KeyboardButton("Чистка брусчатки")
        ],
        [
            KeyboardButton("Чистка плитки"),
            KeyboardButton("Газонокосилка")
        ],
        [
            KeyboardButton("Мойка фасада"),
            KeyboardButton("Дезинфекция")
        ],
        [
            KeyboardButton("Стирка и глажка штор"),
            KeyboardButton("Назад 🔙")
        ],
    ],
    resize_keyboard=True
)

settings_btn_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Изменить номер телефона 📞"),
            KeyboardButton("Изменить имя и фамилию 👤")
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
            KeyboardButton(text="Статистика 📊"),
        ],
    ],
    resize_keyboard=True
)
