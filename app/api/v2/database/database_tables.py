"""
Creating Data Tables
"""

users_table = """ CREATE TABLE IF NOT EXISTS users(
    user_id serial PRIMARY KEY NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255) NOT NULL,
    role INTEGER DEFAULT NULL,
    created_at timestamp default current_timestamp
);"""

categories_table = """ CREATE TABLE IF NOT EXISTS categories(
    category_id serial PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NULL,
    created_at timestamp default current_timestamp
);"""

categories_items = """ CREATE TABLE IF NOT EXISTS category_items(
    category_item_id serial PRIMARY KEY NOT NULL,
    product_id INTEGER NOT NULL,
    category_id INTEGER  NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON UPDATE CASCADE ON DELETE CASCADE
);"""

products_table = """ CREATE TABLE IF NOT EXISTS products(
    product_id serial PRIMARY KEY NOT NULL,
    name INTEGER NOT NULL,
    description VARCHAR(255) NOT NULL,
    quantity INTEGER NOT NULL,
    minimum_inventory VARCHAR(255) NOT NULL,
    price INTEGER NOT NUll,
    created_at timestamp with time zone DEFAULT now()
    );
"""

sales_table = """ CREATE TABLE IF NOT EXISTS sales(
    sale_id serial PRIMARY KEY NOT NULL,
    attendant_email VARCHAR(255) NOT NULL,
    total INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now()
    );
"""

sale_item = """ CREATE TABLE IF NOT EXISTS sale_items(
    sale_item_id serial PRIMARY KEY NOT NULL,
    sale_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    created_at timestamp with time zone DEFAULT now(),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (sale_id) REFERENCES sales (sale_id)
    ON UPDATE CASCADE ON DELETE CASCADE
    );
"""


blacklisted_tokens_table = """ CREATE TABLE IF NOT EXISTS blacklisted(
    black_id serial PRIMARY KEY NOT NULL,
    token VARCHAR(255) NOT NULL,
    created_at timestamp with time zone DEFAULT now()
); """

drop_users_table = """ DROP TABLE IF EXISTS users CASCADE
"""
drop_categories_table = """ DROP TABLE IF EXISTS categories CASCADE
"""
drop_products_table = """ DROP TABLE IF EXISTS products CASCADE
"""
drop_sales = """ DROP TABLE IF EXISTS sales CASCADE
"""
drop_blacklisted_tokens_table = """ DROP TABLE IF EXISTS blacklisted CASCADE
"""
drop_sale_item = """ DROP TABLE IF EXISTS sale_items CASCADE
"""
drop_categories_items = """ DROP TABLE IF EXISTS category_items CASCADE
"""


tables_to_drop = [drop_users_table, drop_categories_table, drop_products_table,
                  drop_sales, drop_blacklisted_tokens_table,
                  drop_categories_items, drop_sale_item]

list_of_tables = [users_table, categories_table, products_table, sales_table,
                  blacklisted_tokens_table, sale_item, categories_items]
