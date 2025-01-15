# tkinter.Button.grid

# Definition: Button is positioned in the grid in the widget.

# Syntax: tkinter.Button.grid  / Button.grid
"""
Options:
Button.grid(
    column = number - use call identifier with given column (string with 0)
    columnsopan = number - this widget will span several columns
    in = master - use master to contain this widget
    in_ master - see 'in' option description
    ipadx = amount - add internal padding in x direction
    ipady = amount - add internal padding in y direction
    padx = amount - add padding in X direction
    pady = amount - add padding in y direction
    row = number - use cell identified with given row(starting with 0)
    rowspan = number - this widget will span several rows
    sticky = NSEW - if call is larger on which side will this widget stick to the call boundary
  )
"""

# Example:
# The code created Label, Entry, and button with defined parameters of row and column in grid

from tkinter import *

master = Tk()
master.title("Grid Widget")

label = Label(master, text = "First Name", font=10)
label.grid(row=0)
entry = Entry(master)
entry.grid(row=0, column=1)

label = Label(master, text="Last Name", font=10)
label.grid(row=1)
entry = Entry(master)
entry.grid(row=1, column=1)

button1 = Button(master, text="Submit")
button1.grid(row=2, column=1)

master.mainloop()
