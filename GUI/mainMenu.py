import tkinter as tk

# Creates the menu along with its dimensions
window = tk.Tk()
window.geometry("1040x700")

def addClass():
    print("Add a class")

def dropClass():
    print("Drop a class")

def searchClass():
    print("Search for a class")

def main():
    # Commands below create the buttons with its dimensions, along with what actions they will perform
    addClassCommand = tk.Button(text="Add a class", command=lambda: addClass(), height=2, width=20)
    dropClassCommand = tk.Button(text="Drop a class", command=lambda: dropClass(), height=2, width=20)
    searchClassCommand = tk.Button(text="Search a class", command=lambda: searchClass(), height=2, width=20)

    # Places the buttons onto the window
    addClassCommand.grid(row=0, column=0)
    dropClassCommand.grid(row=1, column=0)
    searchClassCommand.grid(row=2, column=0)

    window.mainloop()

main()