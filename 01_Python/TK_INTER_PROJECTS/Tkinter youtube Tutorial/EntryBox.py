# Entry Box:
from tkinter import *

root = Tk()
root.title("EntryBox")

# Label
NameLabel = Label(root, text="Name: ")
NameLabel.grid(row=0, column=0)

# Entry
EntryBox = Entry(root)
EntryBox.grid(row=0, column=1)

root.mainloop()
