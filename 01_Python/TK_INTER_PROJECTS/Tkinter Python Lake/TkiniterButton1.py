# tkinter.Button

# Definition: The syntax returns button in the widget.

# Syntax: tkinter.Button()

# Syntax Options:
"""
Button(activebackground, activeforeground, anchor, background, bitmap, borderwidth, cursor,
        disableforeground, font, foreground, highlightbackground, highlightcolor, highlightthickness,
        image, justify, padx, pady, relief, repeatdelay, repeatinterval, takefocus, text, textvariable,
        underline, wraplength)
"""

# Widget Options: Button(command, compound, default, height, overrelief, state, width)

# Example: The method return with the Button positioned in the grid.

from tkinter import *

master = Tk()
master.grid()

button1 = Button(master, text="B1")
button1.grid(row=1, column=0)

button2 = Button(master, text="B2")
button2.grid(row=1, column=2)

button3 = Button(master, text="B3")
button3.grid(row=0, column=1)

button4 = Button(master, text="B4")
button4.grid(row=2, column=1)

master.mainloop()
