# Label with grid function
from tkinter import *

root = Tk()
root.title("Label with Grid ")

# Creating the Labels
label1 = Label(root, text="Label-1")
label2 = Label(root, text="Label-2")
label3 = Label(root, text="Label-3")
# Assign Grid for the Labels
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0)


root.mainloop()
