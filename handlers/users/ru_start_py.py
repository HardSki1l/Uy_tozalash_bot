from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.button import *
from keyboards.default.ru_button import menu_btn_ru, change_language_ru, phone_number_btn_ru, lokatsion_ru, \
    nam_xizmatlar_btn_ru
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
Добро пожаловать, {user[0][5]}

Рады приветствовать вас в нашем боте ✋🏼
""", reply_markup=menu_btn_ru)
    else:
        await message.answer(
            f"Здравствуйте, <i>{message.from_user.full_name}</i>👤!\nВыберите желаемый язык\n\nChoose your preferred language🇺🇿",
            reply_markup=change_language_ru)


@dp.message_handler(text="Узбекча🇺🇿")
async def uzb_starthandler(message: types.Message):
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
