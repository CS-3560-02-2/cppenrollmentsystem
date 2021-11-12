import sqlite3
import os
from sqlite3.dbapi2 import Error


# Get the directory of the current file
CURRENT_DIR = os.path.dirname(__file__)
# Set the db path to current directory
DB_PATH = os.path.join(CURRENT_DIR, "enrollmentsystem.db")
CONN_ERROR = "Error while connecting to sqlite"
CONN_CLOSED = "The SQLite connection is closed"
COURSES_TABLE = """CREATE TABLE IF NOT EXISTS courses (
                course_id INTEGER NOT NULL UNIQUE,
                subject TEXT NOT NULL,
                course_num INTEGER NOT NULL,
                course_title TEXT NOT NULL,
                course_description TEXT,
                course_units INTEGER NOT NULL,
                course_prereq INTEGER,
                PRIMARY KEY (course_id),
                FOREIGN KEY (course_prereq) REFERENCES courses (course_id))"""
INSTRUCTORS_TABLE = """CREATE TABLE IF NOT EXISTS instructors (
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
STUDENTS_TABLE = """CREATE TABLE IF NOT EXISTS students (
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
COURSE_SECTIONS_TABLE = """CREATE TABLE IF NOT EXISTS course_sections (
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
COURSE_ENROLLMENTS_TABLE = """CREATE TABLE IF NOT EXISTS course_enrollments (
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                course_section_id INTEGER NOT NULL,
                grade TEXT,
                term TEXT,
                PRIMARY KEY (student_id, course_id, course_section_id),
                FOREIGN KEY (course_id, course_section_id)
                REFERENCES course_sections (course_id, course_section_id),
                FOREIGN KEY (student_id) REFERENCES students (student_id))"""
TABLES = [
    COURSES_TABLE,
    INSTRUCTORS_TABLE,
    STUDENTS_TABLE,
    COURSE_SECTIONS_TABLE,
    COURSE_ENROLLMENTS_TABLE,
]


def create_connection(db_file):
    """Create a database connection to the SQLite database
        specified by db_file

    Args:
        db_file (database file): database file
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as error:
        print(error)
    return conn


# Initialize database if it does not exist
def db_init(connection, tables):
    """Initialises the database file with the provided tables

    Args:
        connection (sqlite3.connect): connection to db
        tables (list): list of tables with sql create statements
    """
    if connection is not None:
        for table in tables:
            create_table(connection, table)
    else:
        print(CONN_ERROR)


def create_table(connection, create_table_sql):
    """Creates a sqlite table from the provided sql statement

    Args:
        connection (sqlite3.connect): connection to db
        create_table_sql (string): sql statement to execute
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


db_init(create_connection(DB_PATH), TABLES)
