import sqlite3
import os
from sqlite3.dbapi2 import OperationalError


class DB:
    """Interface class for executing queries to the database"""

    # Get the directory of the current file
    # Set the db path to current directory
    def __init__(self, database):
        self.curr_dir = os.path.dirname(__file__)
        self.db_path = os.path.join(self.curr_dir, database)

    def execute_script_from_file(self, filename):
        """Executes commands from an sql file

        Args:
            filename (sql file): sql file to execute
        """
        filename = os.path.join(self.curr_dir, filename)
        # Connect to db
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with open(filename, "r", encoding="utf-8") as sql_file:
            sql_script = sql_file.read()

        # all SQL commands (split on ';')
        sql_commands = filter(None, sql_script.split(";"))
        # Execute every command from the input file
        for command in sql_commands:
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                cursor.execute(command)
            except OperationalError as msg:
                print("Command skipped: ", msg)
        conn.commit()
        conn.close()

    def select_student(self, email):
        """Queries db for student information

        Args:
            email (str): Email to search

        Returns:
            Tuple: Information of requested student
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute(
                "SELECT * FROM students WHERE email=?", (email,)
            )  # need the comma after email, to return the tuple, otherwise it will return a single index
            return cursor.fetchone()

    def select_instructor(self, email):
        """Queries db for instructor information

        Args:
            email (str): Email to search

        Returns:
            Tuple: Information of requsted instructor
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute("SELECT * FROM instructors WHERE email=?", (email,))
            return cursor.fetchone()

    def select_courses_count(self):
        """Queries db for count of all courses

        Returns:
            Tuple: Integer count of courses
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute(
                "SELECT COUNT (*) FROM courses"
            )  # count to return the number of courses
            return cursor.fetchone()

    def select_course_subject_count(self, subject):
        """Queries db for the count of courses of a subject

        Args:
            subject (str): Course abbreviation to search

        Returns:
            Tuple: Integer count of courses
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute("SELECT COUNT (*) FROM courses WHERE subject=?", (subject,))
            return cursor.fetchone()

    def select_course(self, subject, course_num):
        """Queries db for course information

        Args:
            subject (str): The subject abbreviation to search
            course_num (int): The course number to search

        Returns:
            Tuple: Course information
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute(
                "SELECT * FROM courses WHERE (subject=? AND course_num=?)",
                (subject, course_num),
            )
            return cursor.fetchone()

    def select_all_sections(self, course_id):
        """Queries db for all sections of a course

        Args:
            course_id (int): course id to search

        Returns:
            List: All section information
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute(
                """SELECT * FROM course_sections 
                    WHERE course_id = ?""",
                (course_id,),
            )
            return cursor.fetchall()

    def select_course_enrollment(self, student_id):
        """Queries db for course enrollment of a student

        Args:
            student_id (int): Student id to search

        Returns:
            List: List of tuples containg course enrollment information

        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        with conn:
            cursor.execute(
                """SELECT * FROM course_enrollments WHERE student_id = ?""",
                (student_id,),
            )
            return cursor.fetchall()

    def insert_course_enrollment(self, student_id, course_id, course_section_id):
        """Inserts a new enrollment into the database

        Args:
            student_id (int): Id of student registering
            course_id (int): Id of course to be registered
            course_section_id (int): Id of course section to be registered

        Returns:
            int: 1 if INSERT succeeds, -1 if INSERT fails
        """
        conn = sqlite3.connect(self.db_path)
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

    def update_course_enrollment(self, student_id, course_id, course_section_id, term):
        """Updates an enrollment in the database

        Args:
            student_id (int): Id of student registering
            course_id (int): Id of course to be registered
            course_section_id (int): Id of course section to be registered
            term (str): Term of enrollment

        Returns:
            int: 1 if UPDATE succeeds, -1 if INSERT fails
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute(
                    """
                UPDATE course_enrollments
                SET course_id = ?, course_section_id = ?
                WHERE student_id = ?
                (?,?,?)""",
                    (course_id, course_section_id, student_id),
                )
                return 1
        except sqlite3.IntegrityError:
            return -1

    def delete_course_enrollment(self, student_id, course_id, course_section_id, term):
        """Deletes an enrollment in the database

        Args:
            student_id (int): Id of student registering
            course_id (int): Id of course to be registered
            course_section_id (int): Id of course section to be registered
            term (str): Term of enrollment

        Returns:
            int: 1 if DELETE succeeds, -1 if INSERT fails
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            with conn:
                cursor.execute(
                    """
                DELETE FROM course_enrollments
                WHERE student_id = ?, course_id = ?, course_section_id = ?, term = ?
                (?,?,?,?)""",
                    (student_id, course_id, course_section_id, term),
                )
                return 1
        except sqlite3.IntegrityError:
            return -1


if __name__ == "__main__":
    db = DB("enrollmentsystem.db")
    db.execute_script_from_file("enrollmentsystem.db.sql")
