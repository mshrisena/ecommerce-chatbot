import sqlite3

conn = sqlite3.connect('ecommerce.db')
c = conn.cursor()

# Users table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
''')

# Products table
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT,
        image_url TEXT
    )
''')

# Chat History table
c.execute('''
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        message TEXT,
        response TEXT,
        timestamp TEXT
    )
''')

# Add 5 mock products
products = [
    ("Laptop X", "electronics", 59999.0, "High performance laptop", "https://via.placeholder.com/100"),
    ("Cotton T-Shirt", "textiles", 499.0, "Comfortable cotton t-shirt", "https://via.placeholder.com/100"),
    ("Python Book", "books", 999.0, "Learn Python programming", "https://via.placeholder.com/100"),
    ("Gaming Mouse", "electronics", 1999.0, "Ergonomic gaming mouse", "https://via.placeholder.com/100"),
    ("Bedsheet Set", "textiles", 1499.0, "King size bedsheet", "https://via.placeholder.com/100")
]

c.executemany("INSERT INTO products (name, category, price, description, image_url) VALUES (?, ?, ?, ?, ?)", products)

conn.commit()
conn.close()
# This script initializes the database and creates necessary tables.
# It also inserts 5 mock products into the products table.