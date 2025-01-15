from tkinter import *

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)


# Main Menues:
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=filemenu)
menubar.add_cascade(label="View", menu=filemenu)
menubar.add_cascade(label="Help", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
