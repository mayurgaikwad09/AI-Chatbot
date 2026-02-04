import sqlite3
from datetime import datetime

DB_NAME = "chat_history.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

# ✅ THIS FUNCTION WAS MISSING
def save_chat_with_time(user_message, bot_reply):
    conn = get_connection()
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    cursor.execute(
        "INSERT INTO chats (user_message, bot_reply, timestamp) VALUES (?, ?, ?)",
        (user_message, bot_reply, timestamp)
    )
    conn.commit()
    conn.close()

# ✅ THIS FUNCTION WAS MISSING
def clear_chat():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chats")
    conn.commit()
    conn.close()

# Create table automatically
create_table()
