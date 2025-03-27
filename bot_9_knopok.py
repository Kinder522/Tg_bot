from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message ,ReplyKeyboardMarkup,KeyboardButton
from Config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
data = []

for i in range(9):
    data.append(KeyboardButton(text=str(i)))

keyboard = ReplyKeyboardMarkup(keyboard=[[data[0]],[data[1]],[data[2]],[data[3]],[data[4]],[data[5]],[data[6]],[data[7]],[data[8]]],resize_keyboard=True,one_time_keyboard=True)

@dp.message(Command(commands=["start"]))
async def start(message:Message):
    await message.answer(text="Привет!Я бот c 9 кнопками")

dp.run_polling(bot)