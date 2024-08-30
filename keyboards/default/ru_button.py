from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonRequestUser

change_language_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Узбекча🇺🇿"),
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
            KeyboardButton("Очистка Нама 💧")
        ],
        [
            KeyboardButton("Общее очищение 🏚"),
            KeyboardButton("Очистка RoboClenda 🤖")
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
            KeyboardButton("Удаление пыли с ковра"),
            KeyboardButton("Удаление пыли с ковра")
        ],
        [
            KeyboardButton("Удаление пыли с обоев"),
            KeyboardButton("Удаление пыли с жалюзи")
        ],
        [
            KeyboardButton("Удаление пыли с потолка"),
            KeyboardButton("Очищение ванной")
        ],
        [
            KeyboardButton("Очищение туалета"),
            KeyboardButton("Очищение окон")
        ],
        [
            KeyboardButton("Очищение мебели"),
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
            KeyboardButton("Очищение санузла"),
            KeyboardButton("Очищение окон")
        ],
        [
            KeyboardButton("Очищение мебели")
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
            KeyboardButton("Удаление пыли с жалюзи")
        ],
        [
            KeyboardButton("Удаление пыли с потолка"),
            KeyboardButton("Очищение ванной")
        ],
        [
            KeyboardButton("Очищение туалета"),
            KeyboardButton("Очищение окон")
        ],
        [
            KeyboardButton("Очищение мебели"),
            KeyboardButton("Стирка ковров на месте")
        ],
        [
            KeyboardButton("Чистка диванов"),
            KeyboardButton("Чистка матрасов")
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
            KeyboardButton("Упорядочение одежды")
        ],
        [
            KeyboardButton("Упорядочение подвала"),
            KeyboardButton("Упорядочение вещей")
        ],
        [
            KeyboardButton("Утюжка одежды"),
            KeyboardButton("Чистка ковров")
        ],
        [
            KeyboardButton("Чистка холодильника"),
            KeyboardButton("Газонокосилка")
        ],
        [
            KeyboardButton("Мойка фасада"),
            KeyboardButton("Дезинфекция")
        ],
        [
            KeyboardButton("Стирка и утюжка штор"),
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
