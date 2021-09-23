"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from function import trans
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1643782174:AAFIKqsZXE01DQDDkoKeoun1CnDt7WhlDCk'



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Hi {message.from_user.full_name}!\n Welcome to Latin cyrilic bot")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"For Restart /help")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.reply(trans(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)