from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    phone_number = State()
    location = State()
    fullname = State()
    image = State()
    text = State()

class Register_ru(StatesGroup):
    phone_number = State()
    location = State()
    fullname = State()
    image = State()
    text = State()


class Takliflar(StatesGroup):
    textlar = State()


class Takliflar_ru(StatesGroup):
    textlar = State()


class Category(StatesGroup):
    name = State()

class Category_ru(StatesGroup):
    name = State()


