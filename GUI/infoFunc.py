if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

from string import capwords
from data.db import DB


class util:
    def __init__(self, userEntry):
        self.db = DB("enrollmentsystem.db")
        length = len(userEntry)
        if length < 3:
            self.searched_course = self.db.select_course_detail_by_subject(userEntry)
        else:
            self.searched_course = self.db.select_course_detail_by_title(userEntry)

    def addClass(self, courseSectionID, studentID):
        addStudentClass(courseSectionID, studentID)

    def dropClass(self, courseSectionID, studentID):
        dropStudentClass(courseSectionID, studentID)

    def getNumberOfClassesName(self, userEntryName):
        return self.db.select_course_title_count(userEntryName.title())

    def getNumberOfClassesSubject(self, userEntrySubject):
        return self.db.select_course_subject_count(userEntrySubject.upper())

    def getNumberOfClassesStudentID(self, StudentID):
        return self.db.select_course_enrollment_count(StudentID)

    def getCourseID(self):
        course_ids = []
        for index in self.searched_course:
            course_ids.append(index[0])
        return course_ids

    def getSubject(self):
        subjects = []
        for index in self.searched_course:
            subjects.append(index[1])
        return subjects

    def getCourseNum(self):
        course_nums = []
        for index in self.searched_course:
            course_nums.append(index[2])
        return course_nums

    def getCourseTitle(self):
        titles = []
        for index in titles:
            titles.append(index[3])
        return titles

    def getCourseSectionID(self):
        section_ids = []
        for index in self.searched_course:
            section_ids.append(index[4])
        return section_ids

    def getScheduleDays(self):
        days = []
        for index in self.searched_course:
            days.append(index[5])
        return days

    def getStartTime(self):
        start_times = []
        for index in self.searched_course:
            start_times.append(index[6])
        return start_times

    def getEndTime(self):
        end_times = []
        for index in self.searched_course:
            end_times.append(index[7])
        return end_times

    def getIntructorName(self):
        names = []
        for index in self.searched_course:
            names.append(index[8])
        return names

    def getCourseUnits(self):
        units = []
        for index in self.searched_course:
            units.append(index[9])
        return units
