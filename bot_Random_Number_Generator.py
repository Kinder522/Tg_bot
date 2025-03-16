from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message ,ReplyKeyboardMarkup,KeyboardButton
from Config import BOT_TOKEN
import random

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
ready = KeyboardButton(text='1-10')
not_ready = KeyboardButton(text='1-100')
diaposon_3 = KeyboardButton(text='1-1000')
keyboard = ReplyKeyboardMarkup(keyboard=[[ready], [not_ready],[diaposon_3]],resize_keyboard=True,one_time_keyboard=True)

@dp.message(Command(commands=["start"]))
async def start(message:Message):
   
    await message.answer(text="Привет!Я бот который смог😎😎😎",
        reply_markup=keyboard)

@dp.message(F.text == "1-10")
async def one_ten(message:Message):
    await message.answer(str(random.randint(1,10)))
    await message.answer("Ешё нада?")

@dp.message(F.text == "1-100")
async def one_ten(message:Message):
    await message.answer(str(random.randint(1,100)))
    await message.answer("Ешё нада?")

@dp.message(F.text == "1-1000")
async def one_ten(message:Message):
    await message.answer(str(random.randint(1,1000)))
    await message.answer("Ешё нада?")

@dp.message(F.text != "1-10" and F.text != "1-100"and F.text != "1-1000" and F.text.lower() != "да")
async def one_ten(message:Message):
    await message.answer("Я таким не промышляю!!!")
@dp.message(F.text.lower() == "да")
async def again(message:Message):
    await message.answer(text="Ну давай,выбирай",
        reply_markup=keyboard)

dp.run_polling(bot)