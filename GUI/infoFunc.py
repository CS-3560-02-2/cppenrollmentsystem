if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

from string import capwords
from data.db import DB


class util:
    """Utility class to call db query functions. Connects to the database through the DB interface class."""

    def __init__(self, userEntry):
        """Constructor for util class.


        Args:
            userEntry (str): search parameter provided by user
        """
        self.db = DB("enrollmentsystem.db")
        length = len(userEntry)
        if length < 3:
            self.searched_course = self.db.select_course_detail_by_subject(userEntry)
        else:
            self.searched_course = self.db.select_course_detail_by_title(userEntry)

    def addClass(self, courseID, courseSectionID, studentID):
        """Adds a course to a student's enrollment

        Args:
            courseID (int): Course id
            courseSectionID (int): Section id
            studentID (int): Student id
        """
        self.db.insert_course_enrollment(courseID, courseSectionID, studentID)

    def dropClass(self, courseID, courseSectionID, studentID):
        """Removes a course from a student's enrollment

        Args:
            courseID (int): Course id
            courseSectionID (int): Section id
            studentID (int): Student id
        """
        self.db.delete_course_enrollment(courseID, courseSectionID, studentID)

    def getNumberOfClassesName(self, userEntryName):
        """Returns the number of classes when searched by name

        Args:
            userEntryName (str): Title searched by user

        Returns:
            Tuple: Tuple containing the count
        """
        return self.db.select_course_title_count(userEntryName.title())

    def getNumberOfClassesSubject(self, userEntrySubject):
        """Returns the number of classes when searched  by subject

        Args:
            userEntrySubject (str): Subject searched by user

        Returns:
            Tuple: Tuple containing the count
        """
        return self.db.select_course_subject_count(userEntrySubject.upper())

    def getNumberOfClassesStudentID(self, StudentID):
        """Returns the number of classes the student is enrolled in

        Args:
            StudentID (int): Student's id

        Returns:
            Tuple: Tuple containing the count
        """
        return self.db.select_course_enrollment_count(StudentID)

    def getCourseID(self):
        """Gets a list of course ids returned by the course search

        Returns:
            List: list of course ids
        """
        course_ids = []
        for index in self.searched_course:
            course_ids.append(index[0])
        return course_ids

    def getSubject(self):
        """Gets a list of subjects returned by the course search

        Returns:
            List: list of subject strings
        """
        subjects = []
        for index in self.searched_course:
            subjects.append(index[1])
        return subjects

    def getCourseNum(self):
        """Gets a list of course numbers returned by the course search

        Returns:
            List: list of int course numbers
        """
        course_nums = []
        for index in self.searched_course:
            course_nums.append(index[2])
        return course_nums

    def getCourseTitle(self):
        """Gets a list of course titles returned by the course search

        Returns:
            List: list of string course titles
        """
        titles = []
        for index in titles:
            titles.append(index[3])
        return titles

    def getCourseSectionID(self):
        """Gets a list of course section ids returned by the course search

        Returns:
            List: list of int course section ids
        """
        section_ids = []
        for index in self.searched_course:
            section_ids.append(index[4])
        return section_ids

    def getScheduleDays(self):
        """Gets a list of section meeting days returned by the course search

        Returns:
            List: list of string section meeting days
        """
        days = []
        for index in self.searched_course:
            days.append(index[5])
        return days

    def getStartTime(self):
        """Gets a list of section start times returned by the course search

        Returns:
            List: list of str section start times
        """
        start_times = []
        for index in self.searched_course:
            start_times.append(index[6])
        return start_times

    def getEndTime(self):
        """Gets a list of section end times returned by the course search

        Returns:
            List: list of str section end times
        """
        end_times = []
        for index in self.searched_course:
            end_times.append(index[7])
        return end_times

    def getIntructorName(self):
        """Gets a list of instructor names returned by the course search

        Returns:
            List: list of str instructor names
        """
        names = []
        for index in self.searched_course:
            names.append(index[8])
        return names

    def getCourseUnits(self):
        """Gets a list of course units returned by the course search

        Returns:
            List: list of int course units
        """
        units = []
        for index in self.searched_course:
            units.append(index[9])
        return units
