if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.getcwd())

import tkinter as tk
from tkinter import *

sID = ""


def getID():
    global sID
    return sID


def enterID(studentEntry, top):
    global sID
    sID = studentEntry
    top.destroy()


def studentMenu(top):
    deleteGrid(top, 0, 0)
    deleteGrid(top, 0, 1)
    studentMessage = tk.Label(top, text="Enter your student email address")
    studentEntry = Entry(top)
    studentConfirmation = tk.Button(
        top, text="Enter", command=lambda: enterID(studentEntry, top)
    )

    studentMessage.grid(row=0, column=0)
    studentEntry.grid(row=1, column=0)
    studentConfirmation.grid(row=1, column=1)


def teachMenu():
    print("Teacher Menu")


def initialMenu(top):
    studentCommand = tk.Button(
        top, text="Student", command=lambda: studentMenu(top), height=2, width=20
    )
    teacherCommand = tk.Button(
        top, text="Professor", command=lambda: teachMenu(), height=2, width=20
    )

    # Places the buttons onto the window
    studentCommand.grid(row=0, column=0)
    teacherCommand.grid(row=1, column=0)


def deleteGrid(top, x, y):
    messageRemoval = top.grid_slaves(row=x, column=y)
    for l in messageRemoval:
        l.destroy()
