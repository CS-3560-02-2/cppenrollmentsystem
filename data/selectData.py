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

def search_course_count():
    with conn:
        cursor.execute("SELECT COUNT (*) FROM courses") #count to return the number of courses
        return cursor.fetchone()

def search_all_courses(subject):
    with conn:
        cursor.execute("SELECT COUNT (*) FROM courses WHERE subject=?", (subject,))
        return cursor.fetchone()

def select_course(subject, course_num):
    with conn:
        cursor.execute("SELECT * FROM courses WHERE subject=?, course_num=?", (subject, course_num,))
        return cursor.fetchone()

def select_all_sections(course_id):
    with conn:
        cursor.execute("SELECT * FROM course_sections WHERE subject=?, course_id=?", (course_id,))
        return cursor.fetchone()
#havent checked yet

conn.close()
