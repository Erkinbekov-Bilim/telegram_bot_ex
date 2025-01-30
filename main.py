from aiogram import executor
import logging
from config import bot, admins, dp
from handlers import commands, fsm_reg_products, send_products, fsm_order_product
import buttons
from db import main_db


async def on_startup(_):
    for admins_id in admins:
        await bot.send_message(chat_id=admins_id, text='Bot started!', reply_markup=buttons.start)

    await main_db.create_db()


async def on_shutdown(_):
    for admins_id in admins:
        await bot.send_message(chat_id=admins_id, text='Bot stopped!')


commands.register_handlers_commands(dp)
fsm_reg_products.register_handlers_fsm_products(dp)
send_products.register_handlers_send_products(dp)
fsm_order_product.register_handlers_fsm_order_product(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)