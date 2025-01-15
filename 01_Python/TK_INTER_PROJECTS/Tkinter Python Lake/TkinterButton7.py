# tkinter.button(command = def print1)
# The button command executed the def print1.

from tkinter import *
import tkinter

master = tkinter.Tk()

def print1():
    tkinter.Label(master, text="Thank you").pack()

frame = tkinter.Label(master, text="Python Lake: Welcome").pack()

button = tkinter.Button(master, text="Submit", command=print1).pack()

master.mainloop()
