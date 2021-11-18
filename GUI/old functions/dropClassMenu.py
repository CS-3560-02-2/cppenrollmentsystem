import tkinter as tk
import tkinter.ttk

window = tk.Tk()
window.geometry("1040x700")

def classDrop():
    print("Class dropped")

def main():
    userMessage = tk.Label(text = "Select a class to drop")
    exClass1 = tk.Label(text = "Class1")
    exClass1drop = tk.Button(text="Drop", command=lambda: classDrop(), height=2, width=20)

    # Class Categories
    courseIDMessage = tk.Label(text="course_id")
    subjectMessage = tk.Label(text="subject")
    courseNumMessage = tk.Label(text="course_num")
    courseTitleMessage = tk.Label(text="course_title")
    courseDescriptionMessage = tk.Label(text="course_description")
    courseUnitMessage = tk.Label(text="course_units")

    userMessage.grid(row=0, column=0)
    exClass1.grid(row=1, column = 0)
    exClass1drop.grid(row=1, column = 1)

    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=1, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=3, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=5, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=7, rowspan=10, sticky='ns')
    tkinter.ttk.Separator(window, orient="vertical").grid(row=3, column=9, rowspan=10, sticky='ns')


    window.mainloop()
main()