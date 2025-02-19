from aiogram import F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from Config import BOT_TOKEN
import random

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
num = 0
wait = False
wait_to_ans = False

user = {'in_game': False,
        'secret_number': None,
        'attempts': 5,
        'total_games': 0,
        'wins': 0}


@dp.message(Command(commands=["start"]))
async def start(message: Message):
    global wait
    await message.answer(
        "Привет!Я бот который играет  с тобой угадай число\n, я загадываю любое число от 1 до 10 и говорю отгадал ты или нет,ты готов?")
    


@dp.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer(
        '''Этот раздел времено недоступен,перезвоните позже'''
    )

@dp.message(Command(commands="stat"))
async def process_stat_command(message: Message):
    await message.answer(f"🎯Доступные попытки: {user['attempts']}(с платной версией 10)\n🎉Всего игр сыграно: {user['total_games']} \n🏆Побед: {user['wins']}")


@dp.message(Command(commands="cancel"))
async def process_cancel_command(message: Message):
    global user
    if user['in_game']:
        user['in_game'] = False
        await message.answer("Эммм нуу окей,как хочешь")
    else:
        await message.answer("Чо ты там отменить пытаешься тупой,эволюцию себе отмени❤❤❤")

@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']))
async def process_positive_answer(message: Message):
    global user,num
    user['in_game'] = True
    num = randomNum()
    await message.answer("Все я загадал,можешь отгадывать")

def randomNum() -> int:
    return random.randint(1,10)

@dp.message()
async def answer(message:Message):
    global num
    if user['in_game']:
        if message.text.isdigit():
            if int(message.text) >= 0 and int(message.text) <= 100:
                if user['attempts'] > 0:
                    if int(message.text) == num :
                        await message.answer("Молодец,угадал,просто тигр❤❤❤")
                        user['in_game'] = False
                    else:
                        await message.answer("Не угадал,попробуй еще😢😢😢")
                        user['attempts'] -= 1
                else:
                    await message.answer("У тебя попыток не осталось,ТУПОЙ")
        else:
            await message.reply("А ну говори нормальным языком,ничего же не понятно")

@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    if user['in_game']:
        await message.answer("Огадывай давай,не хочет он")
    else:
        await message.answer("Ну не хочешь как хочешь,твои проблемы")

dp.run_polling(bot)
