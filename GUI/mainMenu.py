import tkinter as tk
import searchClassMenu
import currentClasses

# Creates the menu along with its dimensions
window = tk.Tk()
window.geometry("1500x1500")

def main():
    # Commands below create the buttons with its dimensions, along with what actions they will perform

    # Primary user message
    userMessage = tk.Label(text="Enter a class name or search by section below")

    # Places the buttons onto the window
    userMessage.grid(row=0, column=6, sticky="w")

    # Search bar methods
    searchClassMenu.searchMenu(window)
    currentClasses.currentClasses(window)
    window.columnconfigure(1, weight=0)
    window.after(1000, currentClasses)
    window.mainloop()

main()