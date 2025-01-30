
from aiogram import Dispatcher, types
from config import bot
import buttons



async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Hi, I'm a bot for managing products and orders. Use /info to find out more", reply_markup=buttons.start)


async def info_bot_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='I am a bot for working with products and orders. Employees can add products and customers can place orders. Use /products and other commands for interaction', reply_markup=buttons.start)


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(info_bot_command, commands=['info'])