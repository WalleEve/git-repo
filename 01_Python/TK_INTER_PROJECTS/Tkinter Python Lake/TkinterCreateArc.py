# The arc is created through tkinter.Canvas().Create_arc() through input().

from tkinter import *
import tkinter

master = tkinter.Tk()
master.title("Create_arc")

def create_arc1():
    canvas = tkinter.Canvas(master, width=250, height=300)
    canvas.pack()

    x1_value = input("Please enter x1 arc value: ")
    x1 = int(x1_value)

    y1_value = input("Please enter y1 arc value: ")
    y1 = int(y1_value)

    x2_value = input("Please enter x2 arc value: ")
    x2 = int(x2_value)

    y2_value = input("Please enter y2 arc value: ")
    y2 = int(y2_value)

    canvas.create_arc(x1, y1, x2, y2)

button = tkinter.Button(master, text="Create Arc", command = create_arc1).pack()

master.mainloop()
