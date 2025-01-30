
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import main_db
from config import admins, bot


class FSMOrderProduct(StatesGroup):
    product_article = State()
    product_size = State()
    product_count = State()
    client_phone = State()
    product_submit = State()


async def start_order_product(message: types.Message):
    await FSMOrderProduct.product_article.set()
    await message.answer('Enter product article', reply_markup=buttons.cancel)

async def set_product_article(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_article'] = message.text

    await FSMOrderProduct.next()

    await message.answer('Enter product size', reply_markup=buttons.cancel)


async def set_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_size'] = message.text

    await FSMOrderProduct.next()
    await message.answer('Enter product count', reply_markup=buttons.cancel)

async def set_product_count(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_count'] = message.text

    await FSMOrderProduct.next()
    await message.answer('Enter client phone', reply_markup=buttons.cancel)

async def set_client_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['client_phone'] = message.text

    await FSMOrderProduct.next()
    await message.answer('Submit order', reply_markup=buttons.submit)

async def submit_order(message: types.Message, state: FSMContext):
    if message.text == 'Submit':
        async with state.proxy() as order_product:
            await main_db.sql_add_order(
                product_article=order_product['product_article'],
                product_size=order_product['product_size'],
                product_count=order_product['product_count'],
                client_phone=order_product['client_phone']
            )

            for admin in admins:
                await bot.send_message(chat_id=admin, text=f'New order!\n'
                                                           f'Product article: {order_product["product_article"]}\n'
                                                           f'Product size: {order_product["product_size"]}\n'
                                                           f'Product count: {order_product["product_count"]}\n'
                                                           f'Client phone: {order_product["client_phone"]}\n')

            await message.answer('Order successfully submitted!', reply_markup=buttons.start)
            await state.finish()

    elif message.text == 'Cancel':
        await message.answer('Adding order canceled', reply_markup=buttons.start)
        await state.finish()

    else:
        await message.answer('Something went wrong')


async def cancel_order(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Adding order canceled', reply_markup=buttons.start)


def register_handlers_fsm_order_product(dp: Dispatcher):
    dp.register_message_handler(cancel_order, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(start_order_product, commands=['order'], state=None)
    dp.register_message_handler(set_product_article, state=FSMOrderProduct.product_article)
    dp.register_message_handler(set_product_size, state=FSMOrderProduct.product_size)
    dp.register_message_handler(set_product_count, state=FSMOrderProduct.product_count)
    dp.register_message_handler(set_client_phone, state=FSMOrderProduct.client_phone)
    dp.register_message_handler(submit_order, state=FSMOrderProduct.product_submit)

