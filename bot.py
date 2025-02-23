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


users = {}


@dp.message(Command(commands=["start"]))
async def start(message: Message):
    global wait
    if message.from_user.id not in users:
        users[message.from_user.id] = {'in_game': False,
            'secret_number': None,
            'attempts': 5,
            'total_games': 0,
            'wins': 0
        }
        await message.answer(
            "Привет!Я бот который играет  с тобой угадай число\n, я загадываю любое число от 1 до 10 и говорю отгадал ты или нет,ты готов?")
    else:
        await message.answer(
            "Привет!Я бот который играет  с тобой угадай число\n, я загадываю любое число от 1 до 10 и говорю отгадал ты или нет,ты готов?")
    


@dp.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer(
        '''Этот раздел времено недоступен,перезвоните позже'''
    )

@dp.message(Command(commands="stat"))
async def process_stat_command(message: Message):
    print(message.from_user.id,users[message.from_user.id])
    if users[message.from_user.id]['in_game']:
        await message.answer(f"🎯Доступные попытки: {users[message.from_user.id]['attempts']}(с платной версией 10)\n🎉Всего игр сыграно: {users[message.from_user.id]['total_games'] + 1} \n🏆Побед: {users[message.from_user.id]['wins']}")
    else:
        await message.answer(f"🎯Доступные попытки: {users[message.from_user.id]['attempts']}(с платной версией 10)\n🎉Всего игр сыграно: {users[message.from_user.id]['total_games']} \n🏆Побед: {users[message.from_user.id]['wins']}")

@dp.message(Command(commands="cancel"))
async def process_cancel_command(message: Message):
    global users
    if users[message.from_user.id]['in_game']:
        users[message.from_user.id]['in_game'] = False
        users[message.from_user.id]['total_games'] += 1
        await message.answer("Эммм нуу окей,как хочешь")
    else:
        await message.answer("Чо ты там отменить пытаешься тупой,эволюцию себе отмени❤❤❤")

@dp.message(F.text.lower().in_(['да', 'давай', 'сыграем', 'игра', 'играть', 'хочу играть']))
async def process_positive_answer(message: Message):
    global users,num
    users[message.from_user.id]['in_game'] = True
    users[message.from_user.id]['attempts'] = 5
    num = randomNum()
    await message.answer("Все я загадал,можешь отгадывать")

def randomNum() -> int:
    return random.randint(1,100)

@dp.message(F.text.lower().in_(['нет', 'не', 'не хочу', 'не буду']))
async def process_negative_answer(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer("Огадывай давай,не хочет он")
    else:
        await message.answer("Ну не хочешь как хочешь,твои проблемы")

@dp.message()
async def answer(message:Message):
    global num
    if users[message.from_user.id]['in_game']:
        if message.text.isdigit():
            if int(message.text) >= 0 and int(message.text) <= 100:
                if users[message.from_user.id]['attempts'] > 0:
                    if int(message.text) == num :
                        await message.answer("Молодец,угадал,просто тигр❤❤❤")
                        users[message.from_user.id]['in_game'] = False
                        users[message.from_user.id]['total_games'] += 1
                        users[message.from_user.id]['wins'] += 1
                    elif int(message.text) > num:
                        await message.answer("Меньше давай,куда гонишь")
                        users[message.from_user.id]['attempts'] -= 1
                    elif int(message.text) < num:
                        await message.answer("Не угадал, Больше нада")
                        users[message.from_user.id]['attempts'] -= 1
                else:
                    await message.answer("У тебя попыток не осталось,НЕ ТУПОЙ,игра закончена,число было " + num)
                    users[message.from_user.id]['in_game'] = False
                    users[message.from_user.id]['total_games'] += 1
        else:
            await message.reply("А ну говори нормальным языком,ничего же не понятно")
    else:
        await message.reply("Я тебя не понял,ты хочешь играть или нет?")


dp.run_polling(bot)
