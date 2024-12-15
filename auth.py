import sqlite3
import bcrypt

def create_connection():
    return sqlite3.connect('database/inventory.db')

def register_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute('''INSERT INTO users (username, password_hash) VALUES (?, ?)''', 
                       (username, password_hash))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    finally:
        conn.close()

def authenticate_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''SELECT password_hash FROM users WHERE username = ?''', (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

