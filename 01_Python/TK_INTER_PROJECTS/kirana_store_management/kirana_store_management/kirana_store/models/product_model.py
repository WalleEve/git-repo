import sqlite3
from kirana_store.config.config import DATABASE_PATH


def create_product_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            stock INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_product(name, stock, price):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (product_name, stock, price) VALUES (?, ?, ?)', (name, stock, price))
    conn.commit()
    conn.close()

def update_product(product_id, name, stock, price):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET product_name=?, stock=?, price=? WHERE product_id=?', (name, stock, price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE product_id=?', (product_id,))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    return products

create_product_table()
