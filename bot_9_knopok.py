from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from Config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
poll_btn = KeyboardButton(
    text='Создать опрос/викторину',
    request_poll=KeyboardButtonPollType()
)
poll_btn1 = KeyboardButton(
    text='Создать викторину',
    request_poll=KeyboardButtonPollType(type='quiz')
)
poll_btn2 = KeyboardButton(
    text='Создать опрос',
    request_poll=KeyboardButtonPollType(type='regular')
)
web_app_btn = KeyboardButton(
    text='VK',
    web_app=WebAppInfo(url="https://vk.com")
)

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, poll_btn1, poll_btn2, web_app_btn, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    print(1)
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )

dp.run_polling(bot)
