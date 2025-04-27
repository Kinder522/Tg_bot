from aiogram import F, Bot, Dispatcher,types
from aiogram.filters import Command
from aiogram.types import Message ,ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from Config import BOT_TOKEN
import json

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
add_record = KeyboardButton(text='Добавить запись')
del_record = KeyboardButton(text='Удалить запись')
watch_record = KeyboardButton(text='Просмотреть записи')
del_all_record = KeyboardButton(text="Удалить все записи")
keyboard = ReplyKeyboardMarkup(keyboard=[[add_record, del_record],[watch_record],[del_all_record]],resize_keyboard=True,one_time_keyboard=True)
data = {}
wait_to_add_record = False
wait_to_del_record = False
all_record = 0

def load_data():
    try:
        with open("diary.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("diary.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
@dp.message(Command(commands=["start"]))
async def start(message:Message):
    await message.answer(text="Привет!Я бот который за тебя ведет личный дневник",reply_markup=keyboard)


@dp.message(F.text == "Добавить запись")
async def add_record_function(message: Message):
    global wait_to_add_record,data
    user_id = str(message.from_user.id)
    data = load_data()

    if user_id not in data:
        data[user_id] = {"records": []}
    await message.answer("Введите текст записи:")
    wait_to_add_record = True


@dp.message(F.text == "Просмотреть записи")
async def watch_record_function(message: Message):
    global data
    user_id = str(message.from_user.id)
    data = load_data()

    if user_id in data and data[user_id]["records"]:
        records = data[user_id]["records"]
        response = "Ваши записи:\n"
        for record in records:
            response += f"{record['id']}. {record['text']}\n"
        await message.answer(response)
    else:
        await message.answer("У вас пока нет записей.")

@dp.message(F.text == "Удалить запись")
async def del_record_function(message: Message):
    global data,wait_to_del_record
    user_id = str(message.from_user.id)
    data = load_data()
    if user_id in data and data[user_id]["records"]:
        records = data[user_id]["records"]
        response = "Ваши записи:\n"
        for record in records:
            response += f"{record['id']}. {record['text']}\n"
        await message.answer(response)
        wait_to_del_record = True

@dp.message()
async def func(message:Message):
    global data,wait_to_add_record,wait_to_del_record
    user_id = str(message.from_user.id)
    if wait_to_add_record: 
        record_id = len(data[user_id]["records"])+1
        data[user_id]["records"].append({"id":record_id,"text":message.text})
        save_data(data)
        await message.answer("Запись добавлена!")
        wait_to_add_record = False
    elif wait_to_del_record:
        try:
            record_id = int(message.text)
            user_data = data[user_id]["records"]
            user_data.pop(record_id-1)
            save_data(data)
            await message.answer("Запись удалена!")
            wait_to_del_record = False
        except ValueError:
            await message.answer("Неверный номер записи.")

dp.run_polling(bot)