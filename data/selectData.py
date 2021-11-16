import sqlite3
from db import DB_PATH


def select_student(email):
    """Queries db for student information

    Args:
        email (str): Email to search

    Returns:
        Tuple: Information of requested student
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            "SELECT * FROM students WHERE email=?", (email,)
        )  # need the comma after email, to return the tuple, otherwise it will return a single index
        return cursor.fetchone()


def select_instructor(email):
    """Queries db for instructor information

    Args:
        email (str): Email to search

    Returns:
        Tuple: Information of requsted instructor
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute("SELECT * FROM instructors WHERE email=?", (email,))
        return cursor.fetchone()


def select_courses_count():
    """Queries db for count of all courses

    Returns:
        Tuple: Integer count of courses
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            "SELECT COUNT (*) FROM courses"
        )  # count to return the number of courses
        return cursor.fetchone()


def select_course_subject_count(subject):
    """Queries db for the count of courses of a subject

    Args:
        subject (str): Course abbreviation to search

    Returns:
        Tuple: Integer count of courses
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute("SELECT COUNT (*) FROM courses WHERE subject=?", (subject,))
        return cursor.fetchone()


def select_course(subject, course_num):
    """Queries db for course information

    Args:
        subject (str): The subject abbreviation to search
        course_num (int): The course number to search

    Returns:
        Tuple: Course information
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            "SELECT * FROM courses WHERE (subject=? AND course_num=?)",
            (subject, course_num),
        )
        return cursor.fetchone()


def select_all_sections(course_id):
    """Queries db for all sections of a course

    Args:
        course_id (int): course id to search

    Returns:
        List: All section information
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            """SELECT * FROM course_sections 
                WHERE course_id = ?""",
            (course_id,),
        )
        return cursor.fetchall()


def select_course_enrollment(student_id):
    """Queries db for course enrollment of a student

    Args:
        student_id (int): Student id to search

    Returns:
        List: List of tuples containg course enrollment information

    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with conn:
        cursor.execute(
            """SELECT * FROM course_enrollments WHERE student_id = ?""", (student_id,)
        )
<<<<<<< HEAD
        return cursor.fetchall()
=======
    return cursor.fetchall()
>>>>>>> 696b8f78c9b4b9ad2e8c39747bee0cf758895a03
