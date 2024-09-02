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
            KeyboardButton("Все услуги 🛠"),
            KeyboardButton("Влажная уборка 💧")
        ],
        [
            KeyboardButton("РобоКленда уборка 🤖")
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
            KeyboardButton("Удаление пыли со всех мест"),
            KeyboardButton("Удаление пыли с ковра")
        ],
        [
            KeyboardButton("Удаление пыли с обоев"),
            KeyboardButton("Удаление пыли с люстр")
        ],
        [
            KeyboardButton("Удаление пыли с потолка"),
            KeyboardButton("Уборка ванной")
        ],
        [
            KeyboardButton("Уборка туалета"),
            KeyboardButton("Мытье окон")
        ],
        [
            KeyboardButton("Удаление пыли с мебели"),
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
            KeyboardButton("Удаление пыли с пола"),
            KeyboardButton("Удаление пыли с ковра")
        ],
        [
            KeyboardButton("Уборка санузла"),
            KeyboardButton("Мытье окон")
        ],
        [
            KeyboardButton("Удаление пыли с мебели")
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
            KeyboardButton("Удаление пыли с пола"),
            KeyboardButton("Удаление пыли с ковра")
        ],
        [
            KeyboardButton("Удаление пыли с обоев"),
            KeyboardButton("Удаление пыли с люстр")
        ],
        [
            KeyboardButton("Удаление пыли с потолка"),
            KeyboardButton("Уборка ванной")
        ],
        [
            KeyboardButton("Уборка туалета"),
            KeyboardButton("Мытье окон")
        ],
        [
            KeyboardButton("Удаление пыли с мебели"),
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
            KeyboardButton("Мытье посуды"),
            KeyboardButton("Уборка одежды")
        ],
        [
            KeyboardButton("Уборка подвала"),
            KeyboardButton("Уборка вещей")
        ],
        [
            KeyboardButton("Глажка одежды"),
            KeyboardButton("Чистка брусчатки")
        ],
        [
            KeyboardButton("Чистка аликафона"),
            KeyboardButton("Косилка газона")
        ],
        [
            KeyboardButton("Мытье фасада"),
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