from mailbox import Message
from venv import logger

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton
from pyexpat.errors import messages

from keyboards.default.button import *
from keyboards.default.ru_button import menu_btn_ru
from loader import dp, bot
from states.states import *
from utils.db_api.databace import *

fake_data = {}



@dp.message_handler(text="Orqaga 🔙" or "Назад 🔙", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    await record_stat(user_id)
    if message.text == "Orqaga 🔙":
        await message.answer(f"""
            Tanlang:
                """, reply_markup=menu_btn)
    else:
        await message.answer(f"""
                    Выберите:
                        """, reply_markup=menu_btn_ru)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    user = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()
    if user:
        await message.answer(f"""
Assalomu aleykum {user[0][5]}

Bizning botimizga xush kelibsiz ✋🏼
""", reply_markup=menu_btn)
    else:
        await message.answer(
            f"Salom, <i>{message.from_user.full_name}</i>👤!\nKerakli tilni tanlang\n\nВыберите желаемый язык🇷🇺",
            reply_markup=change_language)


@dp.message_handler(text="Uzbekcha🇺🇿")
async def uzb_starthandler(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("<b>Telefon</b> raqamingizni yuboring ☎️", reply_markup=phone_number_btn)
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    # print(True)
    contact = message.contact
    user_id = message.from_user.id
    await add_user(user_id, int(contact.phone_number))
    await message.answer("<b>Lokatsiyani🗺</b> yuboring 📍", reply_markup=lokatsion)
    await state.finish()
    await Register.location.set()


@dp.message_handler(state=Register.location, content_types=types.ContentType.LOCATION)
async def location(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    user_id = message.from_user.id
    longitude = message.location.longitude
    latitude = message.location.latitude
    await update_location(user_id, longitude, latitude)
    await message.answer("<b>Ism Familyangizni</b> yuboring 👤",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await Register.fullname.set()
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnamesave(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    user_id = message.from_user.id
    fullname = message.text
    await update_fullname(user_id, fullname)
    await message.answer("Siz muvaffaqiyatli ro'yhatdan o'tdingiz ✅", reply_markup=menu_btn)
    await state.finish()


@dp.message_handler(text='Xizmatlar 💼')
async def xizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=xizmatlar_btn)


@dp.message_handler(text='Генеральная уборка  🛠')
async def jamixizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=jamixizmatlar_btn)
    await Category.name.set()


@dp.message_handler(text='Влажная уборка  💧')
async def namxizmatlarr(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=nam_xizmatlar_btn)
    await Category.name.set()

@dp.message_handler(text="Ijtimoiy Tarmoqlar 🌐")
async def tarmoqlar(message:types.Message):
    from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
    button = InlineKeyboardButton(text="Open link",
                                  url="https://taplink.cc/universal_cleaning_tashkent?from=qr")
    keyboard = InlineKeyboardMarkup().add(button)

    await message.answer("Havolani ochish uchun tugmani bosing:", reply_markup=keyboard)


@dp.message_handler(text='Генеральная уборка с робоклином  🤖')
async def roboclean(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=Roboclean_btn)
    await Category.name.set()


@dp.message_handler(text="Qo'shimcha xizmatlar ➕")
async def qoshimchaxizmat(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=qoshimchaxizmatlar)
    await Category.name.set()


@dp.message_handler(text="Orqaga 🔙" and "Назад 🔙", state="*")
async def back(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    await record_stat(user_id)
    if message.text == "Orqaga 🔙":
      await message.answer(f"""
Tanlang:
    """, reply_markup=menu_btn)
    else:
        await message.answer(f"""
        Выберите:
            """, reply_markup=menu_btn_ru)


@dp.message_handler(text="Sozlamalar ⚙️")
async def settingsuser(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Tanlang ⬇️", reply_markup=settings_btn)


@dp.message_handler(text="Telefon Nomerni O'zgartirish 📞")
async def changephone(message: types.Message):
    await message.answer("Yangi telefon raqamingizni yuboring")
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number)
async def phones(message: types.Message, state: FSMContext):
    phone_number = message.text
    user_id = message.from_user.id
    await record_stat(user_id)
    if phone_number:
        if message.text.startswith("+998"):
            # print(message.text[1:13])
            user_id = message.from_user.id
            await update_phone_number(user_id, phone_number)
            await message.answer("Telefon raqamingiz muvaffaqiyatli o'zgartirildi ✅", reply_markup=settings_btn)
            await state.finish()
        else:
            await message.answer("Telefon raqamingizni +998 bilan boshlanishi kerak ❌")
    else:
        await message.answer("Telefon raqamingizni kiriting ❌")


@dp.message_handler(text="Ism Familyani O'zgartirish 👤")
async def changefullname(message: types.Message):
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Yangi Ism Familyangizni yuboring")
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnames(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    await record_stat(user_id)
    fullname = message.text
    user_id = message.from_user.id
    await update_fullname(user_id, fullname)
    await message.answer("Ism Familyangiz muvaffaqiyatli o'zgartirildi ✅", reply_markup=settings_btn)
    await state.finish()


@dp.message_handler(text="Profilni O'chirish 🗑")
async def deleteaccount(message: types.Message):
    await delete_user(user_id=message.from_user.id)
    user_id = message.from_user.id
    await record_stat(user_id)
    await message.answer("Profilingiz o'chirib yuborildi ✅\n\nYangi profil yaratish uchun /start ni bosing",
                         reply_markup=types.ReplyKeyboardRemove())


@dp.callback_query_handler(state="*", text="tasdiqlash")
async def zakaz(call: types.CallbackQuery, state:FSMContext):
    user_id = call.message.chat.id
    result = cursor.execute("SELECT choises FROM choise_table WHERE user_id=?", (int(user_id),)).fetchone()
    # print(result)

    a = ""
    if result:
        choises = result[0]
        choises_list = choises.split("//")
        for choise in choises_list:
            if choise not in a:
               a += choise + "\n"
    await record_stat(user_id)
    user_id = call.message.chat.id
    keyboard_inline = InlineKeyboardMarkup()
    ha_button = InlineKeyboardButton(text="Ha✅", callback_data=f"ha {user_id}")
    yoq_button = InlineKeyboardButton(text="Yoq❌", callback_data=f"yoq {user_id}")
    keyboard_inline.add(ha_button, yoq_button)

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
        txt += f"""<b>Zakaz👇🏻✅\n\n{category_name}</b>\n\n\n<b>Foydalanuvchi raqami:  <i>+{i[2]}</i>📞</b>\n\n<b>Foydalanuvchi Ismi: <i>{i[5]}👤</i></b>\n\n<b> Lakatsiya 📍:  <a href="{link}">Lalatsiya</a></b>"""
    # print(txt)
    await call.message.answer("Sizning sorovingiz yuborildi✅", reply_markup=menu_btn)
    await bot.send_message(chat_id=-1002173612484, text=txt, reply_markup=keyboard_inline)
    cursor.execute("DELETE FROM choise_table WHERE user_id=?", (int(user_id),))
    connect.commit()
    await state.finish()


@dp.callback_query_handler(state="*",text="radetish")
async def rad(call: types.CallbackQuery):
    user_id = call.from_user.id
    cursor.execute("DELETE FROM choise_table WHERE user_id=?", (int(user_id),))
    connect.commit()

    await call.message.answer("Zakaz rad etildi")
    await call.message.delete()


async def generate_map_link(latitude, longitude):
    base_url = "https://www.google.com/maps?q="
    return f"{base_url}{latitude},{longitude}"


from utils.db_api.databace import category_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# all_category = []



@dp.callback_query_handler(lambda c: c.data and c.data.startswith("ha"))
async def process_ha_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Foydalanuvchi zakazi qabul qilindi✅")
    await callback_query.bot.send_message(user_id, """<b><b>Хурматли мижоз сизнинг буюртмангиз кабул килинди ✅

Тез орада 770808848 / 770404434
Ушбу ракамлар оркали сизга богланишади.</b></b>""")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("yoq"))
async def process_yoq_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.message.from_user.id
    await record_stat(user_id)
    user_id = callback_query.data.split()[1]
    await callback_query.message.answer(f"Foydalanuvchi zakazi rad etildi❌")
    await callback_query.bot.send_message(user_id,
                                          "<b>Sizning zakazingiz qabul qilinmadi❌\n\n⚠️<b>Bizda hozirda bunday hizmat mavjud emas</b></b>")


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


Admins_forBot = 259083453, 2020292717


@dp.message_handler(commands="admin", state="*")
async def admin_panel(message: types.Message, state: FSMContext):
    await state.finish()
    await record_stat(message.from_user.id)
    user = message.from_user.id
    if user in Admins_forBot:
        await message.answer("<b>Siz bu botda adminsiz 📌️</b>", reply_markup=admin_btn)
    else:
        pass


@dp.message_handler(text="Statistika 📊")
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
    text = f"📊 Botdan foydalanish statistikasi:\n" \
           f" ├ Jami foydalanuvchilar: {total_users}\n" \
           f" ├ Bugungi foydalanuvchilar: {today_users}\n" \
           f" ├ Jami so'rovlar: {total_requests}\n" \
           f" └ Bugungi so'rovlar: {today_requests}"
    await message.reply(text)


@dp.message_handler(text="Foydalanuvchilar 👥")
async def check_user(message: types.Message):
    if message.from_user.id in Admins_forBot:
        from openpyxl import Workbook
        from utils.db_api.databace import cursor

        # SQL so'rovini bajarish va natijalarni olish
        cursor.execute("SELECT user_id, phone, fullname FROM users")
        filtered_data = cursor.fetchall()  # So'rov natijalarini olamiz

        # Yangi ish daftarini yaratish
        wb = Workbook()
        ws = wb.active

        # Sarlavha qatorini qo'shish
        ws.append(["User ID", "Phone", "Full Name"])

        # Ma'lumotlarni Excel fayliga yozish
        for row in filtered_data:
            ws.append(row)

        # Excel faylini saqlash
        wb.save("users_data.xlsx")

        with open('/home/shamsiddin/PycharmProjects/Uy_tozalash_bot/users_data.xlsx', 'rb') as file:
            await message.reply_document(document=file, caption="Bu siz so'ragan fayl.")


@dp.message_handler(commands=['reklama'])
async def reklama_command(message: types.Message):
    await message.answer("Iltimos, reklama uchun rasmini yuboring 📸")
    await Register.image.set()

@dp.message_handler(text="Taklif Shikoyatlar ✍️")
async def taklif(message: types.Message):
    await message.answer("<b>Taklif va shikoyatlaringizni kiriting✍️</b>")
    await Takliflar.textlar.set()

@dp.message_handler(state=Takliflar.textlar)
async def handle_takliflar(message: types.Message, state: FSMContext):
    await state.finish()
    my_message=message.text
    await bot.send_message(chat_id=-1002173612484, text=f"Foydalanuvchidan taklif keldi - {message.from_user.full_name}\n\n<b>{my_message}</b>", reply_markup=menu_btn)
    await message.answer("Taklif Shikoyatlaringiz qabul qilindi")



@dp.message_handler(content_types=['photo'], state=Register.image)
async def reklama_image(message: types.Message, state: FSMContext):
    photo = message.photo[-1]
    photo_id = photo.file_id
    await state.update_data(photo_id=photo_id)
    await message.answer("Rasmdan keyingi ma'lumotlarni kiriting 📝")
    await Register.text.set()


@dp.message_handler(state=Register.text)
async def reklama_text(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    photo_id = data.get('photo_id')
    users = cursor.execute("SELECT user_id FROM users").fetchall()
    for user in users:
        await bot.send_photo(chat_id=user[0], photo=photo_id, caption=text)

    await message.answer("Reklama muvaffaqiyatli yuborildi!")
    await state.finish()


@dp.message_handler(state=Category.name)
async def send_group_for_category(message: types.Message, state: FSMContext):
    # print(True)
    user_id = message.from_user.id
    category_name = message.text
    # print(category_name)
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
                                            parse_mode="HTML", reply_markup=savat_btn)
            cursor.execute("UPDATE choise_table SET message_id=? WHERE user_id=?", (new_id.message_id, user_id))
            connect.commit()
        except:
            message_last = await message.answer(tayyor, reply_markup=savat_btn)
            message_id_update = message_last.message_id
            cursor.execute("UPDATE choise_table SET message_id=? WHERE user_id=?", (message_id_update, user_id))
            connect.commit()


    else:
        if message.text == "Orqaga 🔙" or "Назад 🔙":
            await state.finish()
            user_id = message.from_user.id
            await record_stat(user_id)
            if message.text == "Orqaga 🔙":
                await message.answer(f"""
        Tanlang:
            """, reply_markup=menu_btn)
            else:
                await message.answer(f"""
                Выберите:
                    """, reply_markup=menu_btn_ru)
        else:
            await message.answer("Bunday bo'lim mavjud emas")

