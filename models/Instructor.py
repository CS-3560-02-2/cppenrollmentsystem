from models.User import _User


class Instructor(_User):
    """Represents an Instructor

    Inherits from _User

    Args:
        _User (_User): Super

    Attributes:
        instructor_id: An integer representing the instructor id
    """

    def __init__(self, name, email_address, phone_number, address, instructor_id):
        super().__init__(name, email_address, phone_number, address)
        self.instructor_id = instructor_id
