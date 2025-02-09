from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from Config import BOT_TOKEN
import random
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
num = 0
wait = False
wait_to_ans = False
@dp.message(Command(commands=["start"]))
async def start(message: Message):
    global wait
    await message.answer("Привет!Я бот который играет  с тобой угадай число\n, я загадываю люьое число от 1 до 10 и говорю отгадал ты или нет,ты готов?")
    wait = True
    
    

@dp.message(Command(commands=["help"]))
async def help(message: Message):
    await message.answer(
        '''Этот раздел времено недоступен,перезвоните позже'''
        )


@dp.message()
async def send_echo(message: Message):
    if(wait_to_ans == False):
        if (wait == True):
            await number(message)
    else:
        await answer(message)


    

async def ready(func):
    async def wrapper(message: Message):
        global wait
        if message.text.lower() == "да":
            wait = False
            func(message)  
    return wrapper


async def answer(message:Message):
    global wait_to_ans
    if(message.text == str(num)):
        await message.reply("Молодец,ты угадал!!🎉🎉❤")
        wait_to_ans = False
    else:
        await message.reply("Не угадал😢😢,попробуй еще")



@ready
async def number(message : Message):
    global wait_to_ans,num
    num = random.randint(1,10)
    await message.answer("все я загадал,угадывай число")
    wait_to_ans = True

dp.run_polling(bot)