import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = sqlite3.connect("users.db")
    try:
        yield conn
    finally:
        conn.close()

def create_db():
    with get_db_connection() as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        conn.commit()

def add_user(name: str, age: int):
    with get_db_connection() as conn:
        conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
        conn.commit()

def get_user_by_id(user_id: int) -> tuple or None:
    with get_db_connection() as conn:
        cursor = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        return user