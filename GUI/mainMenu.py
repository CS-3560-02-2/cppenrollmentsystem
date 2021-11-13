import tkinter as tk
from tkinter import *
import tkinter.ttk

# Creates the menu along with its dimensions
window = tk.Tk()
window.geometry("1500x1500")

# Adds student class
def addClass():
    # addStudentClass(classID)
    print("Add a class")

# Drops student class
def dropClass():
    # dropStudentClass(classID)
    print("Drop a class")

def searchMenu():
    classNamelabel = tk.Label(text="Enter class name")
    classSearchEntry = tk.Entry()  # Creates an entry box for the user. Requires an enter button to use
    classSearchEntryButton = tk.Button(text="Search", command=lambda: searchClassName(classSearchEntry))

    # Dropdown menu options
    classDropdown = StringVar(window)
    classDropdown.set("Category 1")
    classCategory = OptionMenu(window, classDropdown, "Category 1", "Category 2", "Category 3")
    classCategoryButton = tk.Button(text="Search", command=lambda: searchClassCategory(classCategory))

    # Places objects onto GUI
    classNamelabel.grid(row=1, column=6)
    classSearchEntry.grid(row=1, column=8)
    classSearchEntryButton.grid(row=1, column=10)
    classCategory.grid(row=2, column=6)
    classCategoryButton.grid(row=2, column=10)

# Finds a number of classes that match user input via class name
def searchClassName(userEntry):
    # getNumberOfClasses(userEntry) - Need to get the number of classes retrieved through search results for loop iteration
    # searchIteration(getNumberofClasses(userEntry))
    print("Search class name")

# Finds a number classes that match category input
def searchClassCategory(userEntry):
    # getNumberOfClasses(userEntry) - Need to get the number of classes retrieved through search results for loop iteration
    # searchIteration(getNumberofClasses(userEntry))
    print("Search class category")

# Gets all matching classes and displays them
def searchIteration(userEntry):
    # getCourseID() - Gets the rest of the information
    # getSubject()
    # getCourseNum()
    # getCourseTitle()
    # getCourseDescription()
    # getCourseUnits()
    print("Listing Courses")

def searchExample():
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

def main():
    # Commands below create the buttons with its dimensions, along with what actions they will perform

    # Primary user message
    userMessage = tk.Label(text="Enter a class name or search by section below")

    # Places the buttons onto the window
    userMessage.grid(row=0, column=6, sticky="w")

    # Search bar methods
    searchMenu()
    searchExample()
    currentClasses()

    window.columnconfigure(1, weight=0)

    window.mainloop()

main()