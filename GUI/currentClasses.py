import tkinter as tk
import tkinter.ttk
from infoFunc import util

n = 0
a = 0
b = 5

# Displays current student classes
def currentClasses(window, studentID):

    currentClassUserMessage = tk.Label(text="Your current classes:")
    spacer = tk.Label(text="              ")
    courseIDMessage = tk.Label(text="course_id")
    subjectMessage = tk.Label(text="subject")
    courseNumMessage = tk.Label(text="course_num")
    courseTitleMessage = tk.Label(text="course_title")
    courseSectionID = tk.Label(text="sec_ID")
    daysMessage = tk.Label(text="days")
    startMessage = tk.Label(text="start")
    endMessage = tk.Label(text="end")
    instructorMessage = tk.Label(text="instructor")
    courseUnitMessage = tk.Label(text="units")

    # Places text on screen
    spacer.grid(row=0, column=21)
    courseIDMessage.grid(row=3, column=22)
    subjectMessage.grid(row=3, column=24)
    courseNumMessage.grid(row=3, column=26)
    courseTitleMessage.grid(row=3, column=28)
    courseSectionID.grid(row=3, column=30)
    daysMessage.grid(row=3, column=32)
    startMessage.grid(row=3, column=34)
    endMessage.grid(row=3, column=36)
    instructorMessage.grid(row=3, column=38)
    courseUnitMessage.grid(row=3, column=40)

    generateClasses(window, studentID)
    currentClassUserMessage.grid(row=2, column=20, sticky="w")

    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=23, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=25, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=27, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=29, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=31, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=33, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=35, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=37, rowspan=50, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=39, rowspan=50, sticky='ns')

def generateClasses(window, studentID):
    global n, a, b
    if a > 0:
        while a != 0:
            deleteGrid(window, a, b)
            a -= 1
            b -= 2
    a = 0
    b = 5
    utility = util(studentID)
    n = utility.getNumberOfClassesStudentID(studentID)
    ID = utility.getCourseID()
    Subject = utility.getSubject()
    CourseNum = utility.getCourseNum()
    CourseTitle = utility.getCourseTitle()
    CourseSecID = utility.getCourseSectionID()
    Days = utility.getScheduleDays()
    startTime = utility.getStartTime()
    endTime = utility.getEndTime()
    instructorName = utility.getIntructorName()
    CourseUnits = utility.getCourseUnits()
    while a < n:
        IDLabel = tk.Label(text=ID[a])
        SubjectLabel = tk.Label(text=Subject[a])
        CourseNumLabel = tk.Label(text=CourseNum[a])
        CourseTitleLabel = tk.Label(text=CourseTitle[a])
        CourseSecIDLabel = tk.Label(text=CourseSecID[a])
        DaysLabel = tk.Label(text=Days[a])
        startTimeLabel = tk.Label(text=startTime[a])
        endTimeLabel = tk.Label(text=endTime[a])
        InstructorNameLabel = tk.Label(text=instructorName[a])
        CourseUnitsLabel = tk.Label(text=CourseUnits[a])
        dropClassButton = tk.Button(text="Drop Class", command=lambda: utility.dropClass(ID[a], CourseSecID[a], studentID))

        IDLabel.grid(row=b, column=22)
        SubjectLabel.grid(row=b, column=24)
        CourseNumLabel.grid(row=b, column=26)
        CourseTitleLabel.grid(row=b, column=28)
        CourseSecIDLabel.grid(row=b, column=30)
        DaysLabel.grid(row=b, column=32)
        startTimeLabel.grid(row=b, column=34)
        endTimeLabel.grid(row=b, column=36)
        InstructorNameLabel.grid(row=b, column=38)
        CourseUnitsLabel.grid(row=b, column=40)
        dropClassButton.grid(row=b, column=42)

        a += 1
        b += 2

def deleteGrid(window, a, b):
    messageRemoval = window.grid_slaves(row=a, column=b)
    for l in messageRemoval:
        l.destroy()

'''
def currentClasses():
    currentClassUserMessage = tk.Label(text="Your current classes:")

    courseIDMessage = tk.Label(text="course_id")
    subjectMessage = tk.Label(text="subject")
    courseNumMessage = tk.Label(text="course_num")
    courseTitleMessage = tk.Label(text="course_title")
    courseDescriptionMessage = tk.Label(text="course_description")
    courseUnitMessage = tk.Label(text="course_units")

    # Places text on screen
    courseIDMessage.grid(row=3, column=14)
    subjectMessage.grid(row=3, column=16)
    courseNumMessage.grid(row=3, column=18)
    courseTitleMessage.grid(row=3, column=20)
    courseDescriptionMessage.grid(row=3, column=22)
    courseUnitMessage.grid(row=3, column=24)

    courseIDMessage1 = tk.Label(text="CS140002")
    subjectMessage1 = tk.Label(text="CS")
    courseNumMessage1 = tk.Label(text="1400")
    courseTitleMessage1 = tk.Label(text="Intro to Computer Science")
    courseDescriptionMessage1 = tk.Label(text="Problem-solving methods")
    courseUnitMessage1 = tk.Label(text="4")
    dropClassButton = tk.Button(text="Drop Class", command=lambda: dropClass())
    spacer = tk.Label(text="              ")

    spacer.grid(row=0, column=13)
    courseIDMessage1.grid(row=5, column=14, sticky="w")
    subjectMessage1.grid(row=5, column=16, sticky="w")
    courseNumMessage1.grid(row=5, column=18, sticky="w")
    courseTitleMessage1.grid(row=5, column=20, sticky="w")
    courseDescriptionMessage1.grid(row=5, column=22, sticky="w")
    courseUnitMessage1.grid(row=5, column=24, sticky="w")
    dropClassButton.grid(row=5, column=26, sticky="w")

    currentClassUserMessage.grid(row=2, column=20, sticky="w")

    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=15, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=17, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=19, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=21, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=23, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=25, rowspan=10, sticky='ns')
'''