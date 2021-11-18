import tkinter as tk
import tkinter.ttk

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
    courseDescriptionMessage = tk.Label(text="course_description")
    courseUnitMessage = tk.Label(text="course_units")

    # Places text on screen
    courseIDMessage.grid(row=3, column=14)
    subjectMessage.grid(row=3, column=16)
    courseNumMessage.grid(row=3, column=18)
    courseTitleMessage.grid(row=3, column=20)
    courseDescriptionMessage.grid(row=3, column=22)
    courseUnitMessage.grid(row=3, column=24)

    generateClasses(window, studentID)

    spacer.grid(row=0, column=13)
    currentClassUserMessage.grid(row=2, column=20, sticky="w")

    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=15, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=17, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=19, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=21, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=23, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=25, rowspan=10, sticky='ns')

def generateClasses(window, studentID):
    global n, a, b
    if a > 0:
        while a != 0:
            deleteGrid(window, a, b)
            a -= 1
            b -= 2
    a = 0
    b = 5
    n = getNumberOfClasses(studentID)
    ID = getCurrentCourseID()
    Subject = getCurrentSubject()
    CourseNum = getCurrentCourseNum()
    CourseTitle = getCurrentCourseTitle()
    CourseDesc = getCurrentCourseDescription()
    CourseUnits = getCurrentCourseUnits()
    while a < n:
        IDLabel = tk.Label(text=ID[x])
        SubjectLabel = tk.Label(text=Subject[x])
        CourseNumLabel = tk.Label(text=CourseNum[x])
        CourseTitleLabel = tk.Label(text=CourseTitle[x])
        if len(CourseDesc[x]) > 17:
            shortendedString = CourseDesc[x]
            CourseDesc[x] = shortendedString[0:16] + "..."
            CourseDescLabel = tk.Label(text=CourseDesc[x])
        else:
            CourseDescLabel = tk.Label(text=CourseDesc[x])
        CourseUnitsLabel = tk.Label(text=CourseUnits[x])


        courseIDMessage = tk.Label(text=IDLabel)
        subjectMessage = tk.Label(text=SubjectLabel)
        courseNumMessage = tk.Label(text=CourseNumLabel)
        courseTitleMessage = tk.Label(text=CourseTitleLabel)
        courseDescriptionMessage = tk.Label(text=CourseDescLabel)
        courseUnitMessage = tk.Label(text=CourseUnitsLabel)
        dropClassButton = tk.Button(text="Add Class", command=lambda: dropClass(IDLabel))

        courseIDMessage.grid(row=5, column=14, sticky="w")
        subjectMessage.grid(row=5, column=16, sticky="w")
        courseNumMessage.grid(row=5, column=18, sticky="w")
        courseTitleMessage.grid(row=5, column=20, sticky="w")
        courseDescriptionMessage.grid(row=5, column=22, sticky="w")
        courseUnitMessage.grid(row=5, column=24, sticky="w")
        dropClassButton.grid(row=5, column=26, sticky="w")

        a += 1
        b += 2

# Drops student class
def dropClass():
    dropStudentClass(classID)

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