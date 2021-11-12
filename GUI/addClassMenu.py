import tkinter as tk
import tkinter.ttk

window = tk.Tk()
window.geometry("1040x700")

def addClass(userEntry):
    classCode = userEntry.get()
    print(classCode)

def main():
    userMessage = tk.Label(text="Enter class code below")
    userEntry = tk.Entry() # Creates an entry box for the user. Requires an enter button to use
    entryRetrieverButton = tk.Button(text="Add class", command=lambda: addClass(userEntry), height=2, width=20)
    currentClassesMessage = tk.Label(text="Current Classes")

    # Class Categories
    courseIDMessage = tk.Label(text="course_id")
    subjectMessage = tk.Label(text="subject")
    courseNumMessage = tk.Label(text="course_num")
    courseTitleMessage = tk.Label(text="course_title")
    courseDescriptionMessage = tk.Label(text="course_description")
    courseUnitMessage = tk.Label(text="course_units")

    userMessage.grid(row=0, column=0)
    userEntry.grid(row=1, column=0)
    entryRetrieverButton.grid(row=1, column=1)
    currentClassesMessage.grid(row=2, column=0)

    courseIDMessage.grid(row=3, column=0)
    subjectMessage.grid(row=3, column=2)
    courseNumMessage.grid(row=3, column=4)
    courseTitleMessage.grid(row=3, column=6)
    courseDescriptionMessage.grid(row=3, column=8)
    courseUnitMessage.grid(row=3, column=10)

    # Line separators
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=1, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=3, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=5, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=7, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=9, rowspan=10, sticky='ns')

    window.mainloop()
main()