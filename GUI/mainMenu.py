import tkinter as tk
import searchClassMenu
import currentClasses
import initialMenu
from tkinter import *

# Creates the menu along with its dimensions
window = tk.Tk()
window.geometry("1500x1500")

def main():
    window.withdraw()
    top = Toplevel(window)
    top.geometry("250x100")
    initialMenu.initialMenu(top)
    window.wait_window(top)
    studentID = initialMenu.getID()
    # Primary user message
    userMessage = tk.Label(text="Enter a class name or search by section below")
    # Places the buttons onto the window
    userMessage.grid(row=0, column=6, sticky="w")

    # Search bar methods
    searchClassMenu.searchMenu(window, studentID)
    currentClasses.currentClasses(window, studentID)
    window.columnconfigure(1, weight=0)
    window.after(1000, currentClasses)
    window.deiconify()
    window.mainloop()

main()