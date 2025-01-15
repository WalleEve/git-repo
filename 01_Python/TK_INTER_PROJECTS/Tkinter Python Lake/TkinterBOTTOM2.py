# The button has positioned in LEFT, RIGHT, TOP and BOTTOM in the Tk Widget.

import tkinter

master = tkinter.Tk()
master.title("tkinter.LEFT, RIGHT, TOP, BOTTOM")
master.geometry("450x360")

buttonTop = tkinter.Button(master, text="TOP").pack(side=tkinter.TOP)
buttonLeft = tkinter.Button(master, text="LEFT").pack(side=tkinter.LEFT)
buttonRight = tkinter.Button(master, text="RIGHT").pack(side=tkinter.RIGHT)
buttonBottom = tkinter.Button(master, text="BOTTOM").pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)

master.mainloop()
