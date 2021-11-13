import tkinter as tk

window = tk.Tk()
window.geometry("200x75")

def waitlistAdd():
    print("Added in waitlist")

def waitlistDrop():
    print("Didn't enroll in waitlist")

def main():
    userMessage = tk.Label(text="Class is full. Add onto waitlist?")
    yes = tk.Button(text="Yes", command=lambda: waitlistAdd())
    no = tk.Button(text="No", command=lambda: waitlistDrop())

    userMessage.place(x=20, y=0)
    yes.place(x=50, y=25)
    no.place(x=125, y=25)
    window.mainloop()

main()
