import tkinter as tk

window = tk.Tk()
window.geometry("1040x700")

def addClass(userEntry):
    classCode = userEntry.get()
    print(classCode)

def main():
    userMessage = tk.Label(text="Enter class code below")
    userEntry = tk.Entry() # Creates an entry box for the user. Requires an enter button to use
    entryRetrieverButton = tk.Button(text="Add class", command=lambda: addClass(userEntry), height=2, width=20)

    userMessage.grid(row=0, column=0)
    userEntry.grid(row=1, column=0)
    entryRetrieverButton.grid(row=1, column=1)

    window.mainloop()
main()