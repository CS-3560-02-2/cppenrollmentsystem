from User import _User

class Instructor(_User):
    """Represents an Instructor

    Inherits from _User

    Args:
        _User (_User): Super

    Attributes:
        instructor_id: An integer representing the instructor id
        department: A string representing the instructor's department

    Methods:
        getInstructor_id: Returns instructor's id
        getDepartment: Returns instructor's department

        setInstructor_id: Sets instructor's id to a new one
        setDepartment: Sets instructor's department to a new one
    """

    def __init__(self, first_name, last_name, street, state, zip_code, phone_number, email, instructor_id, department) -> None:
        super().__init__(first_name, last_name, street, state, zip_code, phone_number, email)
        self.instructor_id = instructor_id
        self.department = department

    def getInstructor_id(self):
        return self.instructor_id

    def setInstructor_id(self, iID):
        self.instructor_id = iID

    def getDepartment(self):
        return self.department

    def setDepartment(self, _department):
        self.department = _department