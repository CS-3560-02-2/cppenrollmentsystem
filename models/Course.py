# Class Course

class Course:
    """Represents a course

    Attributes:
    course_name: A string representing the course name
    course_number: An integer representing the course number
    course_description: A string with the course's description
    course_units: An integer representing the number of units
    course_prereq: A list of Courses required to take the course

    """

    def __init__(self, course_name, course_number, course_description, course_units, course_prereq) -> None:
        self.course_name = course_name
        self.course_number = course_number
        self.course_description = course_description
        self.course_units = course_units
        self.course_prereq = course_prereq
