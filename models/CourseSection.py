class CourseSection:
    """Represents a section of a Course


    Attributes:
        student_capacity: An integer indicating the max size of the section
        course_available: A boolean indicating if the section is available to enroll
        course_schedule: The date & time the section meets
    """

    def __init__(self, student_capacity, course_available, course_schedule) -> None:
        self.student_capacity = student_capacity
        self.course_available = course_available
        self.course_schedule = course_schedule
