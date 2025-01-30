
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import buttons
from db import main_db
from config import admins


class FSMRegProducts(StatesGroup):
    product_name = State()
    product_category = State()
    product_size = State()
    product_price = State()
    product_article = State()
    product_photo = State()
    product_submit = State()


async def start_reg_product(message: types.Message):
    if message.from_user.id not in admins:
        await message.answer('You are not authorized to use this command', reply_markup=buttons.start)
    else:
        await FSMRegProducts.product_name.set()
        await message.answer('Enter product name', reply_markup=buttons.cancel)


async def load_product_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_name'] = message.text

    await FSMRegProducts.next()
    await message.answer('Enter product category', reply_markup=buttons.cancel)

async def load_product_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_category'] = message.text

    await FSMRegProducts.next()
    await message.answer('Enter product size', reply_markup=buttons.cancel)

async def load_product_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_size'] = message.text

    await FSMRegProducts.next()
    await message.answer('Enter product price', reply_markup=buttons.cancel)

async def load_product_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_price'] = message.text

    await FSMRegProducts.next()
    await message.answer('Enter product article', reply_markup=buttons.cancel)

async def load_product_article(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_article'] = message.text

    await FSMRegProducts.next()
    await message.answer('Enter product photo', reply_markup=buttons.cancel)

async def load_product_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product_photo'] = message.photo[-1].file_id

    await FSMRegProducts.next()
    await message.answer_photo(photo=data['product_photo'], caption=f'Product name: {data["product_name"]}\n'
                                                                    f'Product category: {data["product_category"]}\n'
                                                                    f'Product size: {data["product_size"]}\n'
                                                                    f'Product price: {data["product_price"]}\n'
                                                                    f'Product article: {data["product_article"]}\n', reply_markup=buttons.submit)

async def submit_product(message: types.Message, state: FSMContext):
    if message.text == 'Submit':
        async with state.proxy() as data:
            await main_db.sql_add_product(
                product_name=data['product_name'],
                product_category=data['product_category'],
                product_size=data['product_size'],
                product_price=data['product_price'],
                product_article=data['product_article'],
                product_photo=data['product_photo']
            )

            await message.answer('Product added', reply_markup=buttons.start)
            await state.finish()

    elif message.text == 'Cancel':
        await message.answer('Adding product canceled', reply_markup=buttons.start)
        await state.finish()

    else:
        await message.answer('Something went wrong')


async def cancel_reg_product(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Adding product canceled', reply_markup=buttons.start)


def register_handlers_fsm_products(dp: Dispatcher):
    dp.register_message_handler(cancel_reg_product, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(start_reg_product, commands=['add_product'], state=None)
    dp.register_message_handler(load_product_name, state=FSMRegProducts.product_name)
    dp.register_message_handler(load_product_category, state=FSMRegProducts.product_category)
    dp.register_message_handler(load_product_size, state=FSMRegProducts.product_size)
    dp.register_message_handler(load_product_price, state=FSMRegProducts.product_price)
    dp.register_message_handler(load_product_article, state=FSMRegProducts.product_article)
    dp.register_message_handler(load_product_photo, content_types=['photo'], state=FSMRegProducts.product_photo)
    dp.register_message_handler(submit_product, state=FSMRegProducts.product_submit)
