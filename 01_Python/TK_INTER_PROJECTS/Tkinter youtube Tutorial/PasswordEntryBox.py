# Create User name and Password Entry box with check button.

from tkinter import *

root = Tk()
root.title("UserLogin")

# Label for name and password
nameLabel = Label(root, text="Name: ")
nameLabel.grid(row=0, column=0, sticky=E)

passwordLabel = Label(root, text="Password: ")
passwordLabel.grid(row=1, column=0, sticky=E)

# Entry Box for name and password
nameEntryBox = Entry(root)
nameEntryBox.grid(row=0, column=1)

passwordEntryBox = Entry(root)
passwordEntryBox.grid(row=1, column=1)

# Remenber Check Box
chkBox = Checkbutton(root, text="Remember Password")
chkBox.grid(columnspan=2)

root.mainloop()
