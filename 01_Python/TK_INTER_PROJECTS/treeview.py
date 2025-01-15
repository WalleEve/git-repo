from tkinter import *
from tkinter import ttk
from psycopg2 import *


def getdata():
    item = treeview.selection()
    for i in item:
        prinit("selected item is ", treeview.item(i, "values")[0])

def deletedata():
    item = treeview.selection()
    treeview.delete(item)

master = Tk()
master.title("Treeview")
master.geometry("300x250+250+200")
master.configure(bg="white")


col = ("name", "surname", "id")
treeview = ttk.Treeview(master, height=5, show="headings", columns=col)

# Adding columns..
treeview.column("name", width=100, anchor=W)
treeview.column("surname", width=100, anchor=W)
treeview.column("id", width=100, anchor=E)

# Adding Heading
treeview.heading('name', text="Name")
treeview.heading('surname', text="Surname")
treeview.heading('id', text="ID No")
treeview.pack(side=TOP, fill=BOTH)

name = ["mahfuze", "elexa", "eva"]
surname  = ["sayed", "cyrus", "sayed"]
ids = [100, 101, 102]

for i in range(3):
    treeview.insert("", i, value=(name[i], surname[i], ids[i]))


Button(master, text="Get Selected Data", command=getdata).pack(side=LEFT, padx=10, pady=10)
Button(master, text="Delete Selected Data", command=deletedata).pack(side=RIGHT, padx=10, pady=10)


master.mainloop()
