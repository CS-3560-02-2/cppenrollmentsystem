import tkinter as tk
import tkinter.ttk
import searchClassMenu

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
    searchClassMenu.searchMenu(window)
    searchClassMenu.searchExample(window)
    currentClasses()

    window.columnconfigure(1, weight=0)

    window.mainloop()

main()