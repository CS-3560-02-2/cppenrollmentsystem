import tkinter as tk

window = tk.Tk()
window.geometry("1040x700")

def classDrop():
    print("Class dropped")

def main():
    userMessage = tk.Label(text = "Select a class to drop")
    exClass1 = tk.Label(text = "Class1")
    exClass1drop = tk.Button(text="Drop", command=lambda: classDrop(), height=2, width=20)

    userMessage.grid(row=0, column=0)
    exClass1.grid(row=1, column = 0)
    exClass1drop.grid(row=1, column = 1)
    window.mainloop()
main()