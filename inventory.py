import sqlite3
from datetime import datetime
import pandas as pd

def create_connection():
    return sqlite3.connect('database/inventory.db')

def add_item(item_name, category, quantity, price, supplier):
    conn = create_connection()
    cursor = conn.cursor()

    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
    INSERT INTO inventory (item_name, category, quantity, price, supplier, date_added)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (item_name, category, quantity, price, supplier, date_added))

    conn.commit()
    conn.close()

def sell_item(item_id, quantity_sold):
    conn = create_connection()
    cursor = conn.cursor()

    conn.execute('BEGIN TRANSACTION;')

    # Check if there's enough stock
    cursor.execute('SELECT quantity FROM inventory WHERE item_id = ?', (item_id,))
    current_quantity = cursor.fetchone()[0]

    if current_quantity >= quantity_sold:
        cursor.execute('''
        UPDATE inventory
        SET quantity = quantity - ?, last_updated = CURRENT_TIMESTAMP
        WHERE item_id = ?''', (quantity_sold, item_id))

        cursor.execute('''
        INSERT INTO transactions (item_id, quantity_changed, date_of_transaction, transaction_type, note)
        VALUES (?, ?, date('now'), 'sale', ?)''', (item_id, -quantity_sold, f'Sold {quantity_sold} items'))

        conn.commit()
    else:
        print("Insufficient stock!")
        conn.rollback()

    conn.close()

def display_inventory():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM inventory", conn)
    conn.close()
    return df

