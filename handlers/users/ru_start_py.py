from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.button import *
from keyboards.default.ru_button import *
from loader import dp, bot
from states.states import *
from utils.db_api.databace import *

fake_data = {}


@dp.message_handler(text="Русский🇷🇺")
async def uzb_starthandler(message: types.Message):
    print(True)
    await message.answer("<b>Отправьте</b> ваш номер телефона ☎️", reply_markup=phone_number_btn_ru)
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    print(True)
    contact = message.contact
    user_id = message.from_user.id
    await add_user(user_id, int(contact.phone_number))
    await message.answer("<b>Отправьте ваше местоположение🗺</b> 📍", reply_markup=lokatsion_ru)
    await state.finish()
    await Register.location.set()


@dp.message_handler(state=Register.location, content_types=types.ContentType.LOCATION)
async def location(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    longitude = message.location.longitude
    latitude = message.location.latitude
    await update_location(user_id, longitude, latitude)
    await message.answer("<b>Отправьте ваше имя и фамилию</b> 👤",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnamesave(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    fullname = message.text
    await update_fullname(user_id, fullname)
    await message.answer("Вы успешно зарегистрировались ✅", reply_markup=menu_btn_ru)
    await state.finish()


@dp.message_handler(text='Услуги 💼')
async def xizmatlarr(message: types.Message):
    await message.answer("Выберите один из видов услуг:", reply_markup=xizmatlar_btn_ru)


@dp.message_handler(text='Все услуги 🛠')
async def jamixizmatlarr(message: types.Message):
    await message.answer("Выберите один из видов услуг:", reply_markup=jamixizmatlar_btn_ru)


@dp.message_handler(text='Очистка Нама 💧')
async def namxizmatlarr(message: types.Message):
    await message.answer("Выберите один из видов услуг:", reply_markup=nam_xizmatlar_btn_ru)


@dp.message_handler(text='Очистка RoboClenda 🤖')
async def roboclean(message: types.Message):
    await message.answer("Выберите один из видов услуг:", reply_markup=Roboclean_btn_ru)


@dp.message_handler(text="Дополнительные услуги ➕")
async def qoshimchaxizmat(message: types.Message):
    await message.answer("Выберите один из видов услуг:", reply_markup=qoshimchaxizmatlar_ru)


@dp.message_handler(text="Назад 🔙", state="*")
async def back(message: types.Message):
    await message.answer(f"""
Выберите:
    """, reply_markup=menu_btn_ru)


@dp.message_handler(text="Настройки ⚙️")
async def settingsuser(message: types.Message):
    await message.answer("Выберите ⬇️", reply_markup=settings_btn_ru)


@dp.message_handler(text="Изменить номер телефона 📞")
async def changephone(message: types.Message):
    await message.answer("Отправьте ваш новый номер телефона")
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number)
async def phones(message: types.Message, state: FSMContext):
    phone_number = message.text
    if phone_number:
        if message.text.startswith("+998"):
            print(message.text[1:13])
            user_id = message.from_user.id
            await update_phone_number(user_id, phone_number)
            await message.answer("Ваш номер телефона успешно изменен ✅", reply_markup=settings_btn_ru)
            await state.finish()
        else:
            await message.answer("Ваш номер телефона должен начинаться с +998 ❌")
    else:
        await message.answer("Введите номер телефона ❌")


@dp.message_handler(text="Изменить имя и фамилию 👤")
async def changefullname(message: types.Message):
    await message.answer("Отправьте ваше новое имя и фамилию")
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnames(message: types.Message, state: FSMContext):
    fullname = message.text
    user_id = message.from_user.id
    await update_fullname(user_id, fullname)
    await message.answer("Ваше имя и фамилия успешно изменены ✅", reply_markup=settings_btn_ru)
    await state.finish()


@dp.message_handler(text="Удалить профиль 🗑")
async def deleteaccount(message: types.Message):
    await delete_user(user_id=message.from_user.id)
    await message.answer("Ваш профиль удален ✅\n\nДля создания нового профиля нажмите /start",
                         reply_markup=types.ReplyKeyboardRemove())


async def generate_map_link(latitude, longitude):
    base_url = "https://www.google.com/maps?q="
    return f"{base_url}{latitude},{longitude}"


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(state=Category.name)
async def send_group_for_category(message: types.Message, state:FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    user_id = message.from_user.id
    keyboard_inline = InlineKeyboardMarkup()
    ha_button = InlineKeyboardButton(text="Да✅", callback_data=f"haa {user_id}")
    yoq_button = InlineKeyboardButton(text="Нет❌", callback_data=f"yooq {user_id}")
    keyboard_inline.add(ha_button, yoq_button)
    global latitude_user_map
    global longitude_user_map
    await state.finish()
    category_name = message.text

    user = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()

    txt = ""
    for i in user:
        latitude_user_map = i[4]
        longitude_user_map = i[3]
    link = await generate_map_link(latitude_user_map,longitude_user_map)
    for i in user:
        txt += f"""<b>Заказ: {category_name}✅</b>\n\n\n<b>Номер пользователя:  <i>+{i[2]}</i>📞</b>\n\n<b>Имя пользователя: <i>{i[5]}👤</i></b>\n\n<b> Локация 📍:  <a href="{link}">Локация</a></b>"""

    print(txt)
    await message.answer("Ваш запрос был отправлен✅")
    await bot.send_message(chat_id = -1002173612484, text=txt, reply_markup=keyboard_inline)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("haa"))
async def process_ha_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Заказ пользователя был принят✅")
    await callback_query.bot.send_message(user_id, "<b>Ваш заказ был принят✅</b>")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("yooq"))
async def process_yoq_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Заказ пользователя был отклонен❌")
    await callback_query.bot.send_message(user_id, "<b>Ваш заказ был отклонен❌\n\n⚠️<b>На данный момент такая услуга не доступна</b></b>")




con = sqlite3.connect(f'{DB_PATH}/stats.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   date DATE)''')

con.commit()


async def record_stat(user_id):
    cur.execute("INSERT INTO stats (user_id, date) VALUES (?, DATE('now'))", (user_id,))
    con.commit()


@dp.message_handler(commands="admin", state="*")
async def admin_panel(message: types.Message , state: FSMContext):
    await state.finish()
    await record_stat(message.from_user.id)
    user = message.from_user.id
    Admins = 259083453, 2020292717
    if user in Admins:
        await message.answer("<b>Вы администратор в этом боте 📌️</b>", reply_markup=admin_btn_ru)
    else:
        pass


@dp.message_handler(text="Статистика 📊")
async def show_stats(message: types.Message):
    await record_stat(message.from_user.id)
    cur.execute("SELECT COUNT(DISTINCT user_id) FROM stats")
    total_users = cur.fetchone()[0]
    cur.execute("SELECT COUNT(DISTINCT user_id) FROM stats WHERE date = DATE('now')")
    today_users = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM stats")
    total_requests = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM stats WHERE date = DATE('now')")
    today_requests = cur.fetchone()[0]
    text = f"📊 Статистика использования бота:\n" \
           f" ├ Всего пользователей: {total_users}\n" \
           f" ├ Сегодняшние пользователи: {today_users}\n" \
           f" ├ Всего запросов: {total_requests}\n" \
           f" └ Сегодняшние запросы: {today_requests}"
    await message.reply(text)
