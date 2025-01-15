# Check Button:
from tkinter import *

root = Tk()
root.title("CheckButton")

# Label
nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=0, column=0)

# Entry Box
entryBox = Entry(root, fg="Blue")
entryBox.grid(row=0, column=1)

# Check Button
chkButton = Checkbutton(root, text="Remember Name")
chkButton.grid(columnspan=2)

root.mainloop()
