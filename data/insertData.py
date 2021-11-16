import sqlite3
from db import DB_PATH


def insert_course_enrollment(student_id, course_id, course_section_id):
    """Inserts a new enrollment into the database

    Args:
        student_id (int): Id of student registering
        course_id (int): Id of course to be registered
        course_section_id (int): Id of course section to be registered

    Returns:
        int: 1 if INSERT succeeds, -1 if INSERT fails
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        with conn:
            cursor.execute(
                """
            INSERT INTO course_enrollments ('student_id', 'course_id', 'course_section_id') VALUES
            (?,?,?)""",
                (student_id, course_id, course_section_id),
            )
            return 1
    except sqlite3.IntegrityError:
        return -1
