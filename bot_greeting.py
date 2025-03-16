from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message ,ReplyKeyboardMarkup,KeyboardButton
from Config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start(message:Message):
    ready = KeyboardButton(text='Как дела?')
    not_ready = KeyboardButton(text='Что ты умеешь?')
    keyboard = ReplyKeyboardMarkup(keyboard=[[ready, not_ready]],resize_keyboard=True,one_time_keyboard=True)
    await message.answer(text="Привет!Я бот и у меня есть 2 кнопки нажми на одну из них,вдруг что то интересное случиться!",
        reply_markup=keyboard)
    
@dp.message(F.text ==  'Как дела?')
async def whatsup(message:Message):
    await message.answer(text="У меня всё отлично! А у тебя?")

@dp.message(F.text == "Что ты умеешь?")
async def what_can_you_do(message:Message):
    await message.answer(text="Я умею отправлять сообщения и нажимать кнопки!")

@dp.message(F.text != 'Как дела?' and F.text != "Что ты умеешь?")
async def what(message:Message):
    await message.answer(text="Я ЖЕ ПРОСИЛ НА КНОПКИ НАЖИМАТЬ!!!😡😡😡")

dp.run_polling(bot)