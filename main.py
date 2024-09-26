from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, WebAppInfo, WebAppData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery

BOT_TOKEN = '6344977244:AAHCLmbUYofIeIWq8B_web8ONfES2SI75jM'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

web_app_button = InlineKeyboardButton(
    text='Web App Приложение',
    web_app=WebAppInfo(url='htpps://mikola-kachaw.github.io')
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[web_app_button]]
)

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Привет! Снизу Web_App приложение, нажми на кнопку👇',
        reply_markup=keyboard
)

if __name__ == '__main__':
    dp.run_polling(bot)

