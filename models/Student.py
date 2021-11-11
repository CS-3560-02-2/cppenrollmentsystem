from models.User import _User

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

    def __init__(self, first_name, last_name, street, state, zip_code, phone_number, email, student_id, major) -> None:
        super().__init__(first_name, last_name, street, state, zip_code, phone_number, email)
        self.student_id = student_id
        self.major = major

    def getStudent_id(self):
        return self.student_id

    def setStudent_id(self, studentID):
        self.student_id = studentID

    def getMajor(self):
        return self.major

    def setMajor(self, _major):
        self.major = _major

