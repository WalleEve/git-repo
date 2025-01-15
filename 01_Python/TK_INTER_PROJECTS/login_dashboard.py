from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import psycopg2
import sys
import os
import math
from PIL import ImageTk, Image
from time import strftime


def login_dashboard():
    # Login Dashboard Frame
    login_Dashboard_Frame= Frame(store_dashboard, bd=2, relief=RIDGE,  bg="crimson")
    login_Dashboard_Frame.place(x=1, y=1, width=498, height=498)
    # Labels
    back_btn = Button(login_Dashboard_Frame, text="Logout", font=("Calibri", 12, 'bold'), bg="crimson").pack( anchor=NE)
    Label(login_Dashboard_Frame, text="STORE DASHBOARD", font=("Calibri", 12, 'bold'), bg="crimson").pack()
    Label(login_Dashboard_Frame, text="Welcome to Store Management", font=("Calibri", 12), bg="crimson").pack()

    # purchase_btn_frame:

    purchase_btn_frame = Frame(login_Dashboard_Frame, bd=2, relief=RIDGE)
    purchase_btn_frame.place(x=10, y=100, width=240, height=200)
    Label(purchase_btn_frame, text="Purchase",image=pur_img).pack(fill=BOTH)
    Button(purchase_btn_frame, text="Purchase",  bd=4, font=("Calibri", 12, 'bold'),  bg="#43CD80").pack( fill=BOTH)

    #Stock_btn_frame
    stock_btn_frame = Frame(login_Dashboard_Frame, bd=2, relief=RIDGE)
    stock_btn_frame.place(x=10, y=299, width=240, height=192)
    Label(stock_btn_frame, text="Stock",image=stoc_img).pack(fill=BOTH)
    Button(stock_btn_frame, text="Stock",  bd=4, font=("Calibri", 12, 'bold'),  bg="#43CD80").pack( fill=BOTH)
    # Sale_btn_frame
    sale_btn_frame = Frame(login_Dashboard_Frame, bd=2, relief=RIDGE)
    sale_btn_frame.place(x=241, y=100, width=240, height=200)
    Label(sale_btn_frame, text="Sale",image=sale_img).pack(fill=BOTH)
    Button(sale_btn_frame, text="Sale",  bd=4, font=("Calibri", 12, 'bold'),  bg="#43CD80").pack( fill=BOTH)

    # Admin_btn_frame
    admin_btn_frame = Frame(login_Dashboard_Frame, bd=2, relief=RIDGE)
    admin_btn_frame.place(x=241, y=299, width=240, height=192)
    Label(admin_btn_frame, text="Admin",image=admin_img).pack(fill=BOTH)
    Button(admin_btn_frame, text="Admin",  bd=4, font=("Calibri", 12, 'bold'), bg="#43CD80").pack( fill=BOTH)



master = Tk()
master.geometry('500x500')
global store_dashboard
global pur_img
global stoc_img
global sale_img
global admin_img

store_dashboard = Toplevel(master)
store_dashboard.title("Dashboard")
store_dashboard.geometry("500x500+200+200")
# IMAGE
pur_img = Image.open("purchase_1.JPG")
pur_img = pur_img.resize((230, 150))
pur_img = ImageTk.PhotoImage(pur_img)

stoc_img = Image.open("Ready_Stock.png")
stoc_img = stoc_img.resize((230, 150))
stoc_img = ImageTk.PhotoImage(stoc_img)

sale_img = Image.open("cust_sale.jpg")
sale_img = sale_img.resize((230, 150))
sale_img = ImageTk.PhotoImage(sale_img)

admin_img = Image.open("user_admin.png")
admin_img = admin_img.resize((230, 150))
admin_img = ImageTk.PhotoImage(admin_img)

login_dashboard()



master.mainloop()
