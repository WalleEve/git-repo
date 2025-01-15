# This app is a Demo for Retail Application:
""" ------------------------------------------
|Date: 13 March 2021
|Logic: Python
|Gui: Tkinter
|Database: Postgres
|**********************************************
|Demo Retail App
| Section1: Login Page
| Section2: Menu Option [Purchage | Sales | Stock]
| Section3:
|       part1: Purchage [Date | Item | Quantity | Price Per Unit]
|       part2: Sales [Date | Item | Quantity | Total Price]
|       part3: Stock [Date | Item | Total Quantity | Total Price]
--------------------------------------------"""

# Import:
from  tkinter import *
import os
from PIL import ImageTk, Image
#import psycopg2
import sys

# Main Screen:
master  = Tk()
master.title("Retail App")
master.geometry('230x400')
master.configure(bg="#003e53")

# Functions:
def login():
    pass





# Import image
img = Image.open("store.jpg")
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)



# Labels:
Label(master, text = "General Retail Store.", font = ("Calibri", 14)).grid(row=0, sticky=N, pady=10)
Label(master, text = "World Famous Store Keeper", font = ("Calibri", 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N,padx=10, pady=15)


# ENTRY FRAME:
btn_frame = Frame(master, width= 80, height = 40, bg= "#003e53")
btn_frame.grid()
# Label
uname = Label(btn_frame, text="User Name: ", fg="white", bg="#003e53", font=("Calibri", 10))
uname.grid(row=4, column=0, sticky=W, pady=2)
pwd = Label(btn_frame, text="Password: ", fg="white", bg="#003e53", font=("Calibri", 10))
pwd.grid(row=5, column=0, sticky=W, pady=2)
# Entry Box:
t_uname = Entry(btn_frame)
t_uname.grid(row=4, column=1, sticky=W, pady=2)
t_pwd = Entry(btn_frame)
t_pwd.grid(row=5, column=1, sticky=W, pady=2)
# Button:
log = Button(btn_frame, text="Login", width=10, command=login)
log.grid(row=6, sticky=W, padx=10, pady=10)




master.mainloop()
