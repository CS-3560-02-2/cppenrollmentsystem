if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

from models.User import _User
from data.db import DB


class Student(_User):
    """Represents a Student

    Inherits from _User

    Args:
        _User (_User): Super

    Attributes:
        student_id: An integer representing the student id
        major: A string representing the student's major

    Methods:
        getStudent_id: Returns student's id
        getMajor: Returns student's major

        setStudent_id: Sets student's id to a new one
        setMajor:Sets student's major to a new one
    """

    def __init__(
        self,
        student_id,
        first_name,
        last_name,
        street,
        city,
        state,
        zip_code,
        phone_number,
        email,
        major,
    ) -> None:
        self.student_id = student_id
        super().__init__(
            first_name, last_name, street, city, state, zip_code, phone_number, email
        )
        self.major = major

    def getStudent_id(self):
        return self.student_id

    def setStudent_id(self, studentID):
        self.student_id = studentID

    def getMajor(self):
        return self.major

    def setMajor(self, _major):
        self.major = _major
