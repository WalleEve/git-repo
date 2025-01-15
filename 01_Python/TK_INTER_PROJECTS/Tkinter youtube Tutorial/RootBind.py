# bind function
from tkinter import *


root = Tk()
root.title("Bind")
root.geometry("200x100")


def LeftClicky(event):
    print("LEFT CLICK PRESSED")

def RightClick(event):
    print("RIGHT CLICK PRESSED")

def ScrollKey(event):
    print("SCROLL KEY PRESSED")

def LeftKey(event):
    print("LEFT ARROW PRESSED")

def RightKey(event):
    print("RIGHT ARROW PRESSED")

root.bind("<Button-1>", LeftClicky)
root.bind("<Button-3>", RightClick)
root.bind("<Button-2>", ScrollKey)
root.bind("<Left>", LeftKey)
root.bind("<Right>", RightKey)

root.mainloop()
