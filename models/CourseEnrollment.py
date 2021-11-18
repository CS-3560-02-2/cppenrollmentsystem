if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

from models.Course import Course
from data.db import DB


class CourseEnrollment:
    """Represents a Student's course enrollment

    An association class between Student and CourseSection

    Attributes:
        grade: A string representing the grade received in the course
        semester: A string representing the semester the student enrolled in the course(Ex: Fall21)
    """

    def __init__(self, grade, semester) -> None:
        self.grade = grade
        self.semester = semester

    def selectCourse(self):
        return Course.selectCourse(self, course_subject, course_number)
