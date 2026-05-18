import sqlite3
from db.config import DB_NAME


def connect_db():
    connection = sqlite3.connect(DB_NAME)
    return connection


def init_db():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)

    connection.commit()
    connection.close()