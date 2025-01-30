

CREATE_TABLE_PRODUCTS = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_category TEXT NOT NULL,
        product_size TEXT NOT NULL,
        product_price TEXT NOT NULL,
        product_article TEXT NOT NULL,
        product_photo TEXT
    )
"""

CREATE_TABLE_ORDER = """
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_article TEXT NOT NULL,
        product_size TEXT NOT NULL,
        product_count INTEGER NOT NULL,
        client_phone TEXT
    )
"""


INSERT_PRODUCT_query = """
    INSERT INTO products (product_name, product_category, product_size, product_price, product_article, product_photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""

INSERT_ORDER_query = """
    INSERT INTO orders (product_article, product_size, product_count, client_phone)
    VALUES (?, ?, ?, ?)
"""

GET_ALL_PRODUCTS_query = """
    SELECT * FROM products
"""