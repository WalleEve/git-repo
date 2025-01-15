# import tkinter module:
from tkinter import *
from tkinter import ttk

# Create main tkinter window:
root = Tk()

# This will create a label weight
l1 = Label(root, text = "Height")
l2 = Label(root, text = "Width")

# Grid method to arrange label
l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

# Entry Weight:
e1 = Entry(root)
e2 = Entry(root)

# This will arange the entry weight:
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

# checkbutton weight:
c1 = Checkbutton(root, text = "Preserve")
c1.grid(row = 2, column = 0, sticky = W , columnspan = 2)


# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"D:\Class\Django\myFirstProject\Tkinter\img1.png")
img1 = img.subsample(2, 2)
# setting image with the help of label
Label(root, image = img1).grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5)

# button widget
b1 = Button(root, text = "Zoom in")
b2 = Button(root, text = "Zoom out")

# arrange button weights:
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)


root.mainloop()
