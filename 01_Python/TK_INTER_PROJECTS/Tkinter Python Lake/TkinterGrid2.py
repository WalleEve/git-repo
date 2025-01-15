# Python.grid
# The Entry.Get() input text verified through Button(command)

from tkinter import *

master = Tk()
master.title("Login")

def validate1():
    if entry.get() == "pythonlake":
        label1 = Label(master, text="Welcome")
        label1.grid(row=0, column=3)
        entry.destroy()
        button.destroy()
        label.destroy()
    else:
        label2 = Label(master, text="You are not authorized", background="red", fg="white")
        label2.grid(row=0, column=3)

label = Label(master, text="Enter your username:")
label.grid(row=0, column=0)

entry = Entry(master)
entry.grid(row=0, column = 1)

button = Button(master, text="Submit", command=validate1)
button.grid(row=0, column=2)

master.mainloop()
