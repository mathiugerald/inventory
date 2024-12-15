import sqlite3

def create_connection():
    return sqlite3.connect('database/inventory.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    # Create inventory table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        supplier TEXT,
        date_added TEXT NOT NULL,
        last_updated TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create users table for authentication
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    # Create transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER NOT NULL,
        quantity_changed INTEGER NOT NULL,
        date_of_transaction TEXT NOT NULL,
        transaction_type TEXT NOT NULL,
        note TEXT,
        FOREIGN KEY(item_id) REFERENCES inventory(item_id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
