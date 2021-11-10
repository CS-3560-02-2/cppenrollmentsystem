import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("1040x700")

def searchClass(userEntry):
    classCode = userEntry.get()
    print(classCode)

def main():
    userMessage = tk.Label(text="Search for class below")
    userEntry = tk.Entry() # Creates an entry box for the user. Requires an enter button to use
    entryRetrieverButton = tk.Button(text="Search class", command=lambda: searchClass(userEntry), height=2, width=20)

    # Drop down menu
    classDropdown = StringVar(window)
    classDropdown.set("Class 1")
    classDatabase = OptionMenu(window, classDropdown, "Class 1", "Class 2", "Class 3")

    userMessage.grid(row=0, column=0)
    userEntry.grid(row=1, column=0)
    entryRetrieverButton.grid(row=1, column=1)
    classDatabase.grid(row=2, column=0)

    window.mainloop()
main()