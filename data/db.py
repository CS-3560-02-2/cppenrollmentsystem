import sqlite3
import datetime

# Initialize database if it does not exist
def db_init():
    try:
        # Create a connection to the database
        # Create database if it does not exist
        conn = sqlite3.connect("data/enrollmentsystem.db")
        cursor = conn.cursor()
        # Create tables
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER NOT NULL UNIQUE,
            course_title TEXT NOT NULL,
            course_description TEXT,
            course_units INTEGER NOT NULL,
            subject TEXT,
            course_prereq INT,
            PRIMARY KEY (course_id),
            FOREIGN KEY (course_prereq) REFERENCES courses (course_id))"""
        )
        conn.commit
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS instructors (
                instructor_id INTEGER NOT NULL UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL,
                department TEXT,
                PRIMARY KEY (instructor_id))"""
        )
        conn.commit
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER NOT NULL UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                street TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL,
                major TEXT,
                PRIMARY KEY (student_id))"""
        )
        conn.commit
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS course_sections (
                course_section_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                room TEXT,
                schedule_days TEXT,
                schedule_time TIME,
                students_enrolled INTEGER, 
                class_capacity INTEGER,
                waitlist_enrolled INTEGER,
                instructor_id INTEGER,
                PRIMARY KEY (course_section_id, course_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id),
                FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id))"""
        )
        conn.commit
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS course_enrollments (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                course_section_id INTEGER NOT NULL,
                grade TEXT,
                term TEXT,
                PRIMARY KEY (student_id, course_id, course_section_id),
                FOREIGN KEY (course_id, course_section_id) REFERENCES course_sections (course_id, course_section_id),
                FOREIGN KEY (student_id) REFERENCES students (student_id))"""
        )
        conn.commit
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


db_init()
