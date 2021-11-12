import sqlite3
from db import DB_PATH


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def search_student(email):
    with conn:
        cursor.execute("SELECT * FROM students WHERE email=?", (email,)) #need the comma after email, to return the tuple, otherwise it will return a single index
        return cursor.fetchone()


def search_instructor(email):
    with conn:
        cursor.execute("SELECT * FROM instructor WHERE email=?", (email,))
        return cursor.fetchone()

conn.close()
