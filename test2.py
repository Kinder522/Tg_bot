from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message ,ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from Config import BOT_TOKEN
import requests
api_url = 'https://tools.aimylogic.com/api/now?tz=Europe/Moscow&format=dd/MM/yyyy'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
kb_builder = ReplyKeyboardBuilder()
day = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
buttons = [KeyboardButton(text=day[j])for j in range(7)]
buttons.extend(KeyboardButton(text=" ")for i in range(24,29))
buttons.extend(KeyboardButton(text=str(i))for i in range(1,32))
buttons.extend(KeyboardButton(text=" ")for i in range(1,7))
buttons.append(KeyboardButton(text="<"))
buttons.append(KeyboardButton(text=">"))
kb_builder.row(*buttons,width=7)


@dp.message(Command(commands=["start"]))
async def start(message:Message):
    await message.answer(text="Привет!Я бот c календарем",reply_markup=kb_builder.as_markup())

dp.run_polling(bot)