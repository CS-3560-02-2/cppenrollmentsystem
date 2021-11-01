from models.User import _User


class Student(_User):
    """Represents a Student

    Inherits from _User

    Args:
        _User (_User): Super

    Attributes:
        student_id: An integer representing the student id
    """

    def __init__(self, name, email_address, phone_number, address, student_id) -> None:
        super().__init__(name, email_address, phone_number, address)
        self.student_id = student_id
