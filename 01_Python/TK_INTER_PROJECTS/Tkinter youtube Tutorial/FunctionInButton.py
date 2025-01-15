# Function on Button
from tkinter import *

root= Tk()
root.title("Function In Button")

def PrintName():
    print("Hello Sayed")

button1 = Button(root, text="Click Me", fg="Orange", command=PrintName)
button1.pack()

root.mainloop()
