import tkinter as tk

window = tk.Tk()
window.geometry("1040x700")

def studentMenu():
    print("Student Menu")

def teachMenu():
    print("Professor Menu")

def main():
    # Commands below create the buttons with its dimensions, along with what actions they will perform
    studentCommand = tk.Button(text="Student", command=lambda: studentMenu(), height=2, width=20)
    teacherCommand = tk.Button(text="Professor", command=lambda: teachMenu(), height=2, width=20)

    # Places the buttons onto the window
    studentCommand.grid(row=0, column=0)
    teacherCommand.grid(row=1, column=0)

    window.mainloop()

main()