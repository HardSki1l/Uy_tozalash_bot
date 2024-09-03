from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.button import *
from keyboards.default.ru_button import *
from loader import dp, bot
from states.states import *
from utils.db_api.databace import *
from .start import record_stat
fake_data = {}

Admins_forBot = 259083453, 2020292717



@dp.message_handler(text="Русский🇷🇺")
async def rus_starthandler(message: types.Message, state:FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("<b>Отправьте свой номер телефона ☎️</b>", reply_markup=phone_number_btn_ru)
    await Register_ru.phone_number.set()


@dp.message_handler(state=Register_ru.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    contact = message.contact
    user_id = message.from_user.id
    await add_user(user_id, int(contact.phone_number))
    await message.answer("<b>Отправьте свою локацию🗺</b> 📍", reply_markup=lokatsion_ru)
    await state.finish()
    await Register_ru.location.set()




@dp.message_handler(state=Register_ru.location, content_types=types.ContentType.LOCATION)
async def location(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    longitude = message.location.longitude
    latitude = message.location.latitude
    await update_location(user_id, longitude, latitude)
    await message.answer("<b>Отправьте ваше имя и фамилию</b> 👤",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await Register_ru.fullname.set()


@dp.message_handler(state=Register_ru.fullname)
async def fullnamesave(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    fullname = message.text
    await update_fullname(user_id, fullname)
    await message.answer("Вы успешно зарегистрировались ✅", reply_markup=menu_btn_ru)
    await state.finish()


@dp.message_handler(text='Услуги 💼')
async def xizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите одну из услуг:", reply_markup=xizmatlar_btn_ru)


@dp.message_handler(text='Генеральная уборка 🛠')
async def jamixizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите одну из услуг:", reply_markup=jamixizmatlar_btn_ru)
    await Category_ru.name.set()


@dp.message_handler(text='Влажная уборка 💧')
async def namxizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите одну из услуг:", reply_markup=nam_xizmatlar_btn_ru)
    await Category_ru.name.set()


@dp.message_handler(text='Генеральная уборка с робоклином 🤖')
async def roboclean(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите одну из услуг:", reply_markup=Roboclean_btn_ru)
    await Category_ru.name.set()


@dp.message_handler(text="Дополнительные услуги ➕")
async def qoshimchaxizmat(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите одну из услуг:", reply_markup=qoshimchaxizmatlar_ru)
    await Category_ru.name.set()


@dp.message_handler(text="Назад 🔙", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer(f"""
Выберите:
    """, reply_markup=menu_btn_ru)

@dp.message_handler(text="Социальные сети 🌐")
async def set(message:types.Message):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    button = InlineKeyboardButton(text="Открыть ссылку",
                                  url="https://taplink.cc/universal_cleaning_tashkent?from=qr")
    keyboard_ru = InlineKeyboardMarkup().add(button)

    await message.answer("Нажмите кнопку, чтобы открыть ссылку:", reply_markup=keyboard_ru)


@dp.message_handler(text="Настройки ⚙️")
async def settingsuser(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Выберите ⬇️", reply_markup=settings_btn_ru)


@dp.message_handler(text="Изменить номер телефона 📞")
async def changephone(message: types.Message):
    await message.answer("Отправьте новый номер телефона")
    await Register_ru.phone_number.set()


@dp.message_handler(state=Register_ru.phone_number)
async def phones(message: types.Message, state: FSMContext):
    phone_number = message.text
    user_id = message.from_user.id
    await record_stat(user_id)
    if phone_number:
        if message.text.startswith("+998"):
            await update_phone_number(user_id, phone_number)
            await message.answer("Ваш номер телефона успешно изменен ✅", reply_markup=settings_btn_ru)
            await state.finish()
        else:
            await message.answer("Ваш номер телефона должен начинаться с +998 ❌")
    else:
        await message.answer("Введите ваш номер телефона ❌")


@dp.message_handler(text="Изменить имя и фамилию 👤")
async def changefullname(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Отправьте ваше новое имя и фамилию")
    await Register_ru.fullname.set()

@dp.message_handler(text="Предложения и жалобы ✍️")
async def taklif(message: types.Message):
    await message.answer("<b>Введите свои предложения и жалобы✍️</b>")
    await Takliflar_ru.textlar.set()

@dp.message_handler(state=Takliflar_ru.textlar)
async def handle_takliflar(message: types.Message, state: FSMContext):
    await state.finish()
    my_message=message.text
    await bot.send_message(chat_id=-1002173612484, text=f"Получен запрос от пользователя - {message.from_user.full_name}\n\n<b>{my_message}</b>", reply_markup=menu_btn)
    await message.answer("Предложение Ваши жалобы получены")


@dp.message_handler(state=Register_ru.fullname)
async def fullnames(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    fullname = message.text
    await update_fullname(user_id, fullname)
    await message.answer("Ваши имя и фамилия успешно изменены ✅", reply_markup=settings_btn_ru)
    await state.finish()


@dp.message_handler(text="Удалить профиль 🗑")
async def deleteaccount(message: types.Message):
    await delete_user(user_id=message.from_user.id)
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Ваш профиль удален ✅\n\nЧтобы создать новый профиль, нажмите /start",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(state="*", text="tas")
async def zakaz(call: types.CallbackQuery, state: FSMContext):
    user_id = call.message.chat.id
    result = cursor.execute("SELECT choises FROM choise_table WHERE user_id=?", (int(user_id),)).fetchone()

    a = ""
    if result:
        choises = result[0]
        choises_list = choises.split("//")
        for choise in choises_list:
            if choise not in a:
                a += choise + "\n"
    await record_stat(user_id)
    keyboard_inline_ru = InlineKeyboardMarkup()
    ha_button = InlineKeyboardButton(text="Да✅", callback_data=f"da {user_id}")
    yoq_button = InlineKeyboardButton(text="Нет❌", callback_data=f"net {user_id}")
    keyboard_inline_ru.add(ha_button, yoq_button)

    global latitude_user_map
    global longitude_user_map
    category_name = a
    user = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()

    txt = ""
    for i in user:
        latitude_user_map = i[4]
        longitude_user_map = i[3]
    link = await generate_map_link(latitude_user_map, longitude_user_map)
    for i in user:
        txt += f"""<b>Заказ👇🏻✅\n\n{category_name}</b>\n\n\n<b>Номер пользователя:  <i>+{i[2]}</i>📞</b>\n\n<b>Имя пользователя: <i>{i[5]}👤</i></b>\n\n<b> Локация 📍:  <a href="{link}">Локация</a></b>"""

    await call.message.answer("Ваш запрос отправлен✅", reply_markup=menu_btn_ru)
    await bot.send_message(chat_id=-1002173612484, text=txt, reply_markup=keyboard_inline_ru)
    cursor.execute("DELETE FROM choise_table WHERE user_id=?", (int(user_id),))
    connect.commit()
    await state.finish()


@dp.callback_query_handler(state="*", text="rad")
async def rad(call: types.CallbackQuery):
    user_id = call.from_user.id
    cursor.execute("DELETE FROM choise_table WHERE user_id=?", (int(user_id),))
    connect.commit()

    await call.message.answer("Заказ отклонен")
    await call.message.delete()


async def generate_map_link(latitude, longitude):
    base_url = "https://www.google.com/maps?q="
    return f"{base_url}{latitude},{longitude}"


@dp.message_handler(state=Category_ru.name)
async def send_group_for_category(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    category_name = message.text
    message_id = message.message_id
    if category_name in category_all:
        result = await add_choise_category(user_id=user_id, choises=category_name, message_id=message_id)
        tayyor = ''
        for i in result.split('//'):
            if i not in tayyor:
                tayyor += i + "\n"
        try:
            message_get_data = cursor.execute("SELECT message_id FROM choise_table WHERE user_id=?",
                                              (int(user_id),)).fetchone()
            print(message_get_data)
            await bot.delete_message(chat_id=message.from_user.id, message_id=message_get_data[0])
            new_id = await bot.send_message(chat_id=message.from_user.id, text=tayyor,
                                            parse_mode="HTML", reply_markup=savat_btn_ru)
            cursor.execute("UPDATE choise_table SET message_id=? WHERE user_id=?", (new_id.message_id, user_id))
            connect.commit()
        except:
            message_last = await message.answer(tayyor, reply_markup=savat_btn_ru)
            message_id_update = message_last.message_id
            cursor.execute("UPDATE choise_table SET message_id=? WHERE user_id=?", (message_id_update, user_id))
            connect.commit()


    else:
        await message.answer("Такого раздела не существует")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("da"))
async def process_ha_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Заказ пользователя принят✅")
    await callback_query.bot.send_message(user_id, """<b><b>Уважаемый клиент, ваш заказ принят ✅

В ближайшее время с вами свяжутся по номерам 770808848 / 770404434.</b></b>""")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("net"))
async def process_yoq_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Заказ пользователя отклонен❌")
    await callback_query.bot.send_message(user_id,
                                          "<b>Ваш заказ не был принят❌\n\n⚠️<b>На данный момент у нас нет такой услуги</b></b>")


@dp.message_handler(text="Пользователи 👥")
async def check_user(message: types.Message):
    if message.from_user.id in Admins_forBot:
        from openpyxl import Workbook
        from utils.db_api.databace import cursor

        cursor.execute("SELECT user_id, phone, fullname FROM users")
        filtered_data = cursor.fetchall()

        wb = Workbook()
        ws = wb.active

        ws.append(["User ID", "Phone", "Full Name"])

        for row in filtered_data:
            ws.append(row)

        wb.save("users_data.xlsx")

        with open('/home/shamsiddin/PycharmProjects/Uy_tozalash_bot/users_data.xlsx', 'rb') as file:
            await message.reply_document(document=file, caption="Вот запрашиваемый файл.")


@dp.message_handler(commands=['reklama'])
async def reklama_command(message: types.Message):
    await message.answer("Пожалуйста, отправьте изображение для рекламы 📸")
    await Register_ru.image.set()


@dp.message_handler(content_types=['photo'], state=Register_ru.image)
async def reklama_image(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    photo_id = photo.file_id
    await state.update_data(photo_id=photo_id)
    await message.answer("Введите текст для рекламы 📝")
    await Register_ru.text.set()


@dp.message_handler(state=Register_ru.text)
async def reklama_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    photo_id = data.get('photo_id')
    users = cursor.execute("SELECT user_id FROM users").fetchall()
    for user in users:
        await bot.send_photo(chat_id=user[0], photo=photo_id, caption=text)

    await message.answer("Реклама успешно отправлена!")
    await state.finish()