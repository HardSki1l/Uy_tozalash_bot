from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.button import *
from loader import dp
from states.states import *
from utils.db_api.databace import *

fake_data = {}


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    user = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,)).fetchall()
    print(user)
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
    await message.answer("<b>Telefon</b> raqamingizni yuboring ☎️", reply_markup=phone_number_btn)
    await Register.phone_number.set()


@dp.message_handler(state=Register.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number(message: types.Message, state: FSMContext):
    print(True)
    contact = message.contact
    user_id = message.from_user.id
    await add_user(user_id, int(contact.phone_number))
    await message.answer("<b>Lokatsiyani🗺</b> yuboring 📍", reply_markup=lokatsion)
    await state.finish()
    await Register.location.set()


@dp.message_handler(state=Register.location, content_types=types.ContentType.LOCATION)
async def location(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    longitude = message.location.longitude
    latitude = message.location.latitude
    await update_location(user_id, longitude, latitude)
    await message.answer("<b>Ism Familyangizni</b> yuboring 👤",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnamesave(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    fullname = message.text
    await update_fullname(user_id, fullname)
    await message.answer("Siz muvaffaqiyatli ro'yhatdan o'tdingiz ✅", reply_markup=menu_btn)
    await state.finish()


@dp.message_handler(text='Xizmatlar 💼')
async def xizmatlarr(message: types.Message):
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=xizmatlar_btn)


@dp.message_handler(text='Jami xizmlatlar 🛠')
async def jamixizmatlarr(message: types.Message):
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=jamixizmatlar_btn)


@dp.message_handler(text='Nam tozalash 💧')
async def namxizmatlarr(message: types.Message):
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=nam_xizmatlar_btn)


@dp.message_handler(text='RoboClenda tozalash 🤖')
async def roboclean(message: types.Message):
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=Roboclean_btn)


@dp.message_handler(text="Qo'shimcha xizmatlar ➕")
async def qoshimchaxizmat(message: types.Message):
    await message.answer("Xizmatlar turidan birini tanlang:", reply_markup=qoshimchaxizmatlar)


@dp.message_handler(text="Orqaga 🔙", state="*")
async def back(message: types.Message):
    await message.answer(f"""
Tanlang:
    """, reply_markup=menu_btn)


@dp.message_handler(text="Sozlamalar ⚙️")
async def settingsuser(message: types.Message):
    await message.answer("Tanlang ⬇️", reply_markup=settings_btn)


@dp.message_handler(text="Telefon Nomerni O'zgartirish 📞")
async def changephone(message: types.Message):
    await message.answer("Yangi telefon raqamingizni yuboring")
    await Register.phone_number.set()


+998996962112


@dp.message_handler(state=Register.phone_number)
async def phones(message: types.Message):
    phone_number = message.text
    if phone_number:
        if message.text.startswith("+998"):
            print(message.text[1:13])
            user_id = message.from_user.id
            await update_phone_number(user_id, phone_number)
            await message.answer("Telefon raqamingiz muvaffaqiyatli o'zgartirildi ✅", reply_markup=settings_btn)
        else:
            await message.answer("Telefon raqamingizni +998 bilan boshlanishi kerak ❌")
    else:
        await message.answer("Telefon raqamingizni kiriting ❌")


@dp.message_handler(text="Ism Familyani O'zgartirish 👤")
async def changefullname(message: types.Message):
    await message.answer("Yangi Ism Familyangizni yuboring")
    await Register.fullname.set()


@dp.message_handler(state=Register.fullname)
async def fullnames(message: types.Message):
    fullname = message.text
    user_id = message.from_user.id
    await update_fullname(user_id, fullname)
    await message.answer("Ism Familyangiz muvaffaqiyatli o'zgartirildi ✅", reply_markup=settings_btn)


@dp.message_handler(text="Profilni O'chirish 🗑")
async def deleteaccount(message: types.Message):
    await delete_user(user_id=message.from_user.id)
    await message.answer("Profilingiz o'chirib yuborildi ✅")
