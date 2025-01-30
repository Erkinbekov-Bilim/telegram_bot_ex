
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from db import main_db
import buttons


async def star_send_products(message: types.Message):
    products = await main_db.sql_get_all_products()
    if products:
        for product in products:
            caption = (f'Product name: {product["product_name"]}\n'
                       f'Product category: {product["product_category"]}\n'
                       f'Product size: {product["product_size"]}\n'
                       f'Product price: {product["product_price"]}\n'
                       f'Product article: {product["product_article"]}\n')

            await message.answer_photo(photo=product['product_photo'], caption=caption, reply_markup=buttons.start)

    else:
        await message.answer('Products not found', reply_markup=buttons.start)



def register_handlers_send_products(dp: Dispatcher):
    dp.register_message_handler(star_send_products, commands=['products'])
