from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from Config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=["start"]))
async def start(message: Message):
    print(message)
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь!")

@dp.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer(
        '''Этот раздел времено недоступен,перезвоните позже'''
        )
answer = False
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

dp.run_polling(bot)