# import tkinter module
from  tkinter import *
from tkinter import ttk

# creating main tkinter window/toplevel
root = Tk()
root.title("Text Box")

#this will create a lable weight
l1 = Label(root, text="First:")
l2 = Label(root, text="Second:")

# grid method to arrange labels in respective rows and columns
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2 )

# entry weight, used to take entry from user
e1 = Entry(root)
e2 = Entry(root)

# this will arange entry weight
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# infinite loop
root.mainloop()
