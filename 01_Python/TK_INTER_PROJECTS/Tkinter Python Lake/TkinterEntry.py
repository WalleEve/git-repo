# The tkinter.Entry is used to check the string characteristics though string methods.

from tkinter import *

master = Tk()
master.title("String methods")

def cap():
    try:
        c = str.capitalize(s.get())
        s.set(c)

    except ValueError:
        pass
def cfold():
    try:
        c = str.casefold(s.get())
        s.set(c)

    except ValueError:
        pass

def ifier():
    try:
        if str.isidentifier(s.get()) == True:
            s.set("Yes")

        else:
            s.set("No")
    except ValueError:
        pass

def ipace():
    try:
        if str.isspace(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass
def iric():
    try:
        if str.isnumeric(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass

def ower():
    try:
        if str.islower(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass

def inum():
    try:
        if str.isalnum(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass
def imal():
    try:
        if str.isdecimal(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass

def igit():
    try:
        if str.isdigit(s.get()) == True:
            s.set("Yes")
        else:
            s.set("No")
    except ValueError:
        pass

def clr():
    try:
        s.set("")
    except ValueError:
        pass


s =StringVar()

entry = Entry(master, textvariable = s)
entry.grid(row = 0, columnspan =4, sticky = W+E)

button_capitalize = Button(master, text="capitalize", width=10, command=cap)
button_capitalize.grid(row = 2, column = 0)


button_casefold=Button(master, text="casefold",width=10, command=cfold)
button_casefold.grid(row=2, column=1)

button_isidentifier=Button(master, text="isidentifier",width=10,command=ifier)
button_isidentifier.grid(row=2, column=2)


button_isspace=Button(master, text="isspace",width=10, command=ipace)
button_isspace.grid(row=3, column=0)

button_endswith=Button(master, text="endswith", width=10, command=iric)
button_endswith.grid(row=3, column=1)

button_islower=Button(master, text="islower",width=10, command=ower)
button_islower.grid(row=3, column=2)



button_isalnum=Button(master, text="isalnum",width=10, command=inum)
button_isalnum.grid(row=4, column=0)

button_isdecimal=Button(master, text="isdecimal",width=10, command=imal)
button_isdecimal.grid(row=4, column=1)

button_isdigit=Button(master, text="isdigit",width=10, command=igit)
button_isdigit.grid(row=4, column=2)

button_clear=Button(master, text="Clear", command=clr )
button_clear.grid(row=5, columnspan=3,sticky=W+E)

master.mainloop()
