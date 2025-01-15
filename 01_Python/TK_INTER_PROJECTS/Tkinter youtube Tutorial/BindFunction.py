# Bind Function:
from tkinter import *

root = Tk()
root.title("Bind Function")

# Function to Call from Button Press:
def PrintName(event):
    print("Hi Sayed")

# Button:
button1 = Button(root, text="Click Me")
button1.bind("<Button-1>", PrintName)
button1.pack()

root.mainloop()
