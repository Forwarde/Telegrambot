from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import types
import app.keyboard as kb
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext

router=Router()


class Register(StatesGroup):
    name=State()
    age=State()
    number=State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!',reply_markup=kb.main)
    await message.reply('How are you?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали кнопку помощи')


# Пример с F(Magic filters) from aiogram import Dispatcher,Bot,F
@router.message(F.text == 'Каталог')
async def nice(message: Message):
    await message.answer("Выберите категорию товара",reply_markup=kb.catalog)

@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: types.CallbackQuery):
    await callback.answer("Вы выбрали категорию",show_alert=True)
    await callback.message.answer("Вы выбрали категорию Футболки")

@router.message(Command("register"))
async def register(message: Message,state:FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")

@router.message(Register.name)
async def register_name(message: Message,state:FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.age)
    await message.answer("Введите ваш возраст")


@router.message(Register.age)
async def register_age(message: Message,state:FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(Register.number)
    await message.answer("Отправьте ваш номер телефона",reply_markup=kb.get_number)

@router.message(Register.number,F.contact)
async def register_number(message: Message,state:FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data=await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\n Ваш возраст: {data["age"]}\n Номер: {data["number"]}')
    await state.clear()
