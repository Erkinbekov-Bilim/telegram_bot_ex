
import sqlite3
from db import queries

db = sqlite3.connect('db/products.sqlite3')
cursor = db.cursor()


async def create_db():
    if db:
        print('create db')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_ORDER)

def get_db_connection():
    conn = sqlite3.connect('db/products.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


async def sql_add_product(product_name, product_category, product_size, product_price, product_article, product_photo):
    cursor.execute(queries.INSERT_PRODUCT_query, (product_name, product_category, product_size, product_price, product_article, product_photo))
    db.commit()

async def sql_add_order(product_article, product_size, product_count, client_phone):
    cursor.execute(queries.INSERT_ORDER_query, (product_article, product_size, product_count, client_phone))
    db.commit()

async def sql_get_all_products():
    conn = get_db_connection()
    products = conn.execute(queries.GET_ALL_PRODUCTS_query).fetchall()
    conn.close()
    return products