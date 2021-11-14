# Class Course


class Course:
    """Represents a course

    Attributes:
    course_name: A string representing the course name
    course_number: An integer representing the course number
    course_description: A string with the course's description
    course_units: An integer representing the number of units
    course_prereq: A list of Courses required to take the course
    course_sections: A list of sections available for the course

    """

    def __init__(
        self,
        course_name,
        course_subject,
        course_number,
        course_description,
        course_units,
        course_prereq,
        course_sections,
        course_ID,
        # I added course_subkect, course_sections, and course_ID
        # course_ID is to return a unique ID to selectCourse and each section has its own ID
    ) -> None:
        self.course_name = course_name
        self.course_subject = course_subject
        self.course_number = course_number
        self.course_description = course_description
        self.course_units = course_units
        self.course_prereq = course_prereq
        self.course_sections = course_sections
        self.course_ID = course_ID

    def selectCourse(self, course_subject, course_number):
        return self.course_ID 

    def selectAllSections(self):
        return self.course_sections