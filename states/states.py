from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class Register(StatesGroup):
    phone_number = State()
    location = State()
    fullname = State()


class Category(StatesGroup):
    name = State()

class Register(StatesGroup):
    phone_number = State()
    location = State()
    fullname = State()
    image = State()
    text = State()
