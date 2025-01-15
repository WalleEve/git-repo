#
from tkinter import *


root = Tk()
root.title("Login Page")
root.geometry("200x200")

def printnUser(event):
    print("Hello We are Working on it...")

def printLogin(event):
    print("Welcome")


topFrame = Frame(root)
topFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

nUserButton = Button(topFrame, text="New User")
nUserButton.bind("<Button-1>", printnUser)
nUserButton.grid(columnspan=2)


nameLabel = Label(bottomFrame, text="User :", fg="Orange")
nameLabel.grid(row=0, column=0, sticky=E)
nameEntryBox = Entry(bottomFrame, fg="Blue")
nameEntryBox.grid(row=0, column=1)

passwordLabel = Label(bottomFrame, text="Password :", fg="Orange")
passwordLabel.grid(row=1, column=0, sticky=E)
passwordEntryBox = Entry(bottomFrame, fg="Blue")
passwordEntryBox.grid(row=1, column=1)

loginButton = Button(bottomFrame, text="Login")
loginButton.bind("<Button-1>", printLogin)
loginButton.grid(columnspan=2)

chkBox = Checkbutton(bottomFrame, text="Remember password")
chkBox.grid(columnspan=2)

root.mainloop()
