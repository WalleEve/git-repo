# The Button has positioned in LEFT, RIGHT, TOP and BOTTOM in the Tk Widget.

import tkinter

master = tkinter.Tk()
master.title("Button Position")
master.geometry("450x350")

buttonLeft = tkinter.Button(master, text="LEFT", fg="Blue").pack(side=tkinter.LEFT)
buttonRight = tkinter.Button(master, text="RIGHT", fg="Red").pack(side=tkinter.RIGHT)
buttonTop = tkinter.Button(master, text="TOP", fg="Green").pack(side=tkinter.TOP)
buttonBottom = tkinter.Button(master, text="BOTTOM", fg="Orange").pack(side=tkinter.BOTTOM)

master.mainloop()
