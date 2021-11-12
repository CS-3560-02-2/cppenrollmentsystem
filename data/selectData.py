import sqlite3
from db import DB_PATH


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def search_student():
    with conn:
        cursor.execute("SELECT * FROM students WHERE email=?", (email))
        print(cursor.fetchone())