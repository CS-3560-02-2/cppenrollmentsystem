if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

import tkinter as tk
from tkinter import *
import tkinter.ttk
import collections
from infoFunc import util

x = 0
y = 5
z = 0


def categorySeparator():
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

    courseIDMessage.grid(row=3, column=0)
    subjectMessage.grid(row=3, column=2)
    courseNumMessage.grid(row=3, column=4)
    courseTitleMessage.grid(row=3, column=6)
    courseSectionID.grid(row=3, column=8)
    daysMessage.grid(row=3, column=10)
    startMessage.grid(row=3, column=12)
    endMessage.grid(row=3, column=14)
    instructorMessage.grid(row=3, column=16)
    courseUnitMessage.grid(row=3, column=18)


def searchMenu(window, studentID):
    categorySeparator()

    classNamelabel = tk.Label(text="Enter class name")
    classSearchEntry = (
        tk.Entry()
    )  # Creates an entry box for the user. Requires an enter button to use
    userSearch = classSearchEntry.get()
    classSearchEntryButton = tk.Button(
        text="Search",
        command=lambda: searchClassName(userSearch, window, studentID),
    )

    # Dropdown menu options
    classDropdown = StringVar(window)
    classDropdown.set("CS")
    classCategory = OptionMenu(window, classDropdown, "CS", "MAT")
    classCategoryButton = tk.Button(
        text="Search",
        command=lambda: searchClassCategory(classCategory, window, studentID),
    )
    # Practice function
    # classCategoryButton = tk.Button(text="Search", command=lambda: practiceFunction(classCategory, window))

    # Places objects onto GUI
    classNamelabel.grid(row=1, column=6)
    classSearchEntry.grid(row=1, column=8)
    classSearchEntryButton.grid(row=1, column=10)
    classCategory.grid(row=2, column=6)
    classCategoryButton.grid(row=2, column=10)

    # Generates a separator
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=1, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=3, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=5, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=7, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=9, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=11, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=13, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=15, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=17, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=19, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="vertical").grid(
        row=3, column=21, rowspan=50, sticky="ns"
    )
    tkinter.ttk.Separator(window, orient="horizontal").grid(
        row=4, column=0, columnspan=30, ipadx=700, sticky="ns"
    )


# Finds a number of classes that match user input via class name
def searchClassName(userEntry, window, studentID):
    utility = util()
    utility.search_courses(userEntry)
    utility.getNumberOfClassesName(
        userEntry
    )  # Need to get the number of classes retrieved through search results for loop iteration
    searchIteration(
        utility.getNumberOfClassesName(userEntry), window, studentID, utility
    )


# Finds a number classes that match category input
def searchClassCategory(userEntry, window, studentID):
    utility = util()
    utility.search_courses(userEntry)
    utility.getNumberOfClassesSubject(
        userEntry
    )  # Need to get the number of classes retrieved through search results for loop iteration
    searchIteration(
        utility.getNumberOfClassesSubject(userEntry), window, studentID, utility
    )


# Gets all matching classes and displays them
def searchIteration(entries, window, studentID, utility):
    global x, y
    if x > 0:
        while x != 0:
            deleteGrid(window, x, y)
            x -= 1
            y -= 2
    # Gets the basic information about the classes
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
    x = 0
    y = 5
    while x < entries:
        IDLabel = tk.Label(text=ID[x])
        SubjectLabel = tk.Label(text=Subject[x])
        CourseNumLabel = tk.Label(text=CourseNum[x])
        CourseTitleLabel = tk.Label(text=CourseTitle[x])
        CourseSecIDLabel = tk.Label(text=CourseSecID[x])
        DaysLabel = tk.Label(text=Days[x])
        startTimeLabel = tk.Label(text=startTime[x])
        endTimeLabel = tk.Label(text=endTime[x])
        InstructorNameLabel = tk.Label(text=instructorName[x])
        CourseUnitsLabel = tk.Label(text=CourseUnits[x])
        addClassButton = tk.Button(
            text="Add Class",
            command=lambda: utility.addClass(ID[x], CourseSecID[x], studentID),
        )

        IDLabel.grid(row=y, column=0)
        SubjectLabel.grid(row=y, column=2)
        CourseNumLabel.grid(row=y, column=4)
        CourseTitleLabel.grid(row=y, column=6)
        CourseSecIDLabel.grid(row=y, column=8)
        DaysLabel.grid(row=y, column=10)
        startTimeLabel.grid(row=y, column=12)
        endTimeLabel.grid(row=y, column=14)
        InstructorNameLabel.grid(row=y, column=16)
        CourseUnitsLabel.grid(row=y, column=18)
        addClassButton.grid(row=y, column=20)

        x += 1
        y += 2


def deleteGrid(window, x, y):
    messageRemoval = window.grid_slaves(row=x, column=y)
    for l in messageRemoval:
        l.destroy()


# This function will take from the test file
"""

def searchExample(window):
    # Creates class identifiers for the user
    courseIDMessage = tk.Label(text="course_id")
    subjectMessage = tk.Label(text="subject")
    courseNumMessage = tk.Label(text="course_num")
    courseTitleMessage = tk.Label(text="course_title")
    courseDescriptionMessage = tk.Label(text="course_description")
    courseUnitMessage = tk.Label(text="course_units")

    # Places text on screen
    courseIDMessage.grid(row=3, column=0)
    subjectMessage.grid(row=3, column=2)
    courseNumMessage.grid(row=3, column=4)
    courseTitleMessage.grid(row=3, column=6)
    courseDescriptionMessage.grid(row=3, column=8)
    courseUnitMessage.grid(row=3, column=10)

    # Example class
    courseIDMessage1 = tk.Label(text="CS140002")
    subjectMessage1 = tk.Label(text="CS")
    courseNumMessage1 = tk.Label(text="1400")
    courseTitleMessage1 = tk.Label(text="Intro to Computer Science")
    courseDescriptionMessage1 = tk.Label(text="Problem-solving methods")
    courseUnitMessage1 = tk.Label(text="4")
    addClassButton = tk.Button(text="Add Class", command=lambda: addClass())

    courseIDMessage1.grid(row=5, column=0)
    subjectMessage1.grid(row=5, column=2)
    courseNumMessage1.grid(row=5, column=4)
    courseTitleMessage1.grid(row=5, column=6)
    courseDescriptionMessage1.grid(row=5, column=8)
    courseUnitMessage1.grid(row=5, column=10)
    addClassButton.grid(row=5, column=12)

    # Generates a separator
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=1, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=3, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=5, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=7, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=9, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=11, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=13, rowspan = 10, sticky='ns')
    tkinter.ttk.Separator(window, orient="horizontal").grid(row=4, column=0, columnspan=30, ipadx=700, sticky='ns')

def practiceFunction(userEntry, window):
    i = 0
    ID = collections.deque([])
    Subject = collections.deque([])
    CourseNum = collections.deque([])
    CourseTitle = collections.deque([])
    CourseDesc = collections.deque([])
    CourseUnits = collections.deque([])
    with open("testCases.txt") as file:
        for line in file:
            currentLine = line.split(",")
            print(str(currentLine[1]))
            ID.append(str(currentLine[0]))
            Subject.append(str(currentLine[1]))
            CourseNum.append(str((currentLine[2])))
            CourseTitle.append(str(currentLine[3]))
            if len(currentLine[4]) > 17:
                shortendedString = str(currentLine[4])
                CourseDesc.append(shortendedString[0:16] + "...")
            else:
                CourseDesc.append(str(currentLine[4]))
            CourseUnits.append(str(currentLine[5]))
    x = 0
    y = 5
    if i == -1:
        print("No results")
    else:
        print("Success")
        while x < 6:
            IDLabel = tk.Label(text=ID[x])
            SubjectLabel = tk.Label(text=Subject[x])
            CourseNumLabel = tk.Label(text=CourseNum[x])
            CourseTitleLabel = tk.Label(text=CourseTitle[x])
            CourseDescLabel = tk.Label(text=CourseDesc[x])
            CourseUnitsLabel = tk.Label(text=CourseUnits[x])

            courseIDMessage = tk.Label(text=IDLabel)
            subjectMessage = tk.Label(text=SubjectLabel)
            courseNumMessage = tk.Label(text=CourseNumLabel)
            courseTitleMessage = tk.Label(text=CourseTitleLabel)
            courseDescriptionMessage = tk.Label(text=CourseDescLabel)
            courseUnitMessage = tk.Label(text=CourseUnitsLabel)
            addClassButton = tk.Button(text="Add Class", command=lambda: addClass())

            courseIDMessage.grid(row=y, column=0)
            subjectMessage.grid(row=y, column=2)
            courseNumMessage.grid(row=y, column=4)
            courseTitleMessage.grid(row=y, column=6)
            courseDescriptionMessage.grid(row=y, column=8)
            courseUnitMessage.grid(row=y, column=10)
            addClassButton.grid(row=y, column=12)

            x += 1
            y += 2
            print(Subject[x])
"""
