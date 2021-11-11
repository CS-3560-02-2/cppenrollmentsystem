import sqlite3
import os


# Get the directory of the current file
CURRENT_DIR = os.path.dirname(__file__)
# Set the db path to current directory
DB_PATH = os.path.join(CURRENT_DIR, "enrollmentsystem.db")


# Initialize database if it does not exist
def db_init():
    """Initializes database"""
    # Create tables
    create_courses_table()
    create_instructors_table()
    create_students_table()
    create_course_sections_table()
    create_course_enrollments_table()


def create_courses_table():
    """Creates courses table if table does not exist

    Raises:
        sqlite3.Error if connection to db fails
    """
    try:
        # Create a connection to the database
        # Create database if it does not exist

        # Connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create table
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER NOT NULL UNIQUE,
            subject TEXT NOT NULL,
            course_num INTEGER NOT NULL,
            course_title TEXT NOT NULL,
            course_description TEXT,
            course_units INTEGER NOT NULL,
            course_prereq INTEGER,
            PRIMARY KEY (course_id),
            FOREIGN KEY (course_prereq) REFERENCES courses (course_id))"""
        )
        conn.commit
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def create_instructors_table():
    """Creates instructors table if table does not exist

    Raises:
        sqlite3.Error if connection to db fails
    """
    try:
        # Create a connection to the database
        # Create database if it does not exist

        # Connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create table
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
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def create_students_table():
    """Creates students table if table does not exist

    Raises:
        sqlite3.Error if connection to db fails
    """
    try:
        # Create a connection to the database
        # Create database if it does not exist

        # Connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create table
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
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def create_course_sections_table():
    """Creates course_sections table if table does not exist

    Raises:
        sqlite3.Error if connection to db fails
    """
    try:
        # Create a connection to the database
        # Create database if it does not exist

        # Connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create table
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS course_sections (
                course_section_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                room TEXT,
                schedule_days TEXT,
                start_time TEXT,
                end_time TEXT,
                students_enrolled INTEGER,
                class_capacity INTEGER,
                waitlist_enrolled INTEGER,
                waitlist_capacity INTEGER,
                instructor_id INTEGER,
                PRIMARY KEY (course_section_id, course_id),
                FOREIGN KEY (course_id) REFERENCES courses (course_id),
                FOREIGN KEY (instructor_id) REFERENCES instructors (instructor_id))"""
        )
        conn.commit
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if conn:
            conn.close()
            print("The SQLite connection is closed")


def create_course_enrollments_table():
    """Creates course_enrollments table if table does not exist

    Raises:
        sqlite3.Error if connection to db fails
    """
    try:
        # Create a connection to the database
        # Create database if it does not exist

        # Connect to db
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Create table
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS course_enrollments (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                course_section_id INTEGER NOT NULL,
                grade TEXT,
                term TEXT,
                PRIMARY KEY (student_id, course_id, course_section_id),
                FOREIGN KEY (course_id, course_section_id)
                REFERENCES course_sections (course_id, course_section_id),
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
