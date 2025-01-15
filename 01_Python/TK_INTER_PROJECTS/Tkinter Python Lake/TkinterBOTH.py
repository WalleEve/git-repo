# tkinter.BOTH:

# The option stretch the Weight to boundaries.

# Syntax: fill = BOTH

# Example: The button width extended to the Widget boundaries.

import tkinter

master = tkinter.Tk()
master.title("tkinter. LEFT, RIGHT, TOP, BOTTOM")
master.geometry("450x360")

buttonLeft = tkinter.Button(master, text="LEFT" )
buttonLeft.pack(side=tkinter.LEFT ,fill=tkinter.BOTH)

buttonRight = tkinter.Button(master, text="RIGHT")
buttonRight.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

buttonTop = tkinter.Button(master, text="TOP")
buttonTop.pack(side=tkinter.TOP, fill=tkinter.BOTH)

buttonBottom = tkinter.Button(master, text="BOTTOM")
buttonBottom.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

master.mainloop()
