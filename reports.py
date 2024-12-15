import pandas as pd
from inventory import create_connection

def export_to_excel(file_name='inventory_report.xlsx'):
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM inventory", conn)
    df.to_excel(file_name, index=False)
    conn.close()

def generate_receipt(transaction_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT t.transaction_id, i.item_name, t.quantity_changed, t.date_of_transaction
    FROM transactions t
    JOIN inventory i ON t.item_id = i.item_id
    WHERE t.transaction_id = ?
    ''', (transaction_id,))

    transaction = cursor.fetchone()

    receipt = f"Receipt ID: {transaction[0]}\n" \
              f"Item Name: {transaction[1]}\n" \
              f"Quantity Sold: {-transaction[2]}\n" \
              f"Date: {transaction[3]}\n"

    print(receipt)

    conn.close()

# Example usage:
# generate_receipt(1)
# export_to_excel()


