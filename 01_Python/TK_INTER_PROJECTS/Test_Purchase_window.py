from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
import psycopg2
import sys
import os
import math



class calc:

    def getandreplace(self):

        """replace x with * and ÷ with /"""
        self.expression = self.e.get()
        self.newtext=self.expression.replace('/','/')
        self.newtext=self.newtext.replace('x','*')


    def equals(self):
        """when the equal button is pressed"""
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value= eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.e.delete(0,END)
            self.e.insert(0,self.value)

    def squareroot(self):
        """squareroot method"""
        self.getandreplace()
        try:
            # evaluate the expression using the eval function
            self.value= eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.sqrtval=math.sqrt(self.value)
            self.e.delete(0,END)
            self.e.insert(0,self.sqrtval)

    def square(self):
        """square method"""
        self.getandreplace()
        try:
            #evaluate the expression using the eval function
            self.value= eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0,END)
            self.e.insert(0,'Invalid Input!')
        else:
            self.sqval=math.pow(self.value,2)
            self.e.delete(0,END)
            self.e.insert(0,self.sqval)

    def clearall(self):
            """when clear button is pressed,clears the text input area"""
            self.e.delete(0,END)

    def clear1(self):
            self.txt=self.e.get()[:-1]
            self.e.delete(0,END)
            self.e.insert(0,self.txt)

    def action(self,argi):
            """pressed button's value is inserted into the end of the text area"""
            self.e.insert(END,argi)

    def __init__(self,calc_frame):
            self.e = Entry(calc_frame, width=30, font=("Calibri", 13))
            self.e.grid(row=0,column=0,columnspan=8,pady=3, padx=5)
            self.e.focus_set() #Sets focus on the input text area

            # Generating Buttons
            Button(calc_frame,text="=",width=11,height=3,fg="blue",
                   bg="orange",command=lambda:self.equals()).grid(
                                     row=4, column=4,columnspan=2)

            Button(calc_frame,text='AC',width=5,height=3,
                          fg="red", bg="light green",
             command=lambda:self.clearall()).grid(row=1, column=4)

            Button(calc_frame,text='C',width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.clear1()).grid(row=1, column=5)

            Button(calc_frame,text="+",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action('+')).grid(row=4, column=3)

            Button(calc_frame,text="x",width=5,height=3,
                    fg="blue",bg="orange",
                    command=lambda:self.action('x')).grid(row=2, column=3)

            Button(calc_frame,text="-",width=5,height=3,
                    fg="red",bg="light green",
                    command=lambda:self.action('-')).grid(row=3, column=3)

            Button(calc_frame,text="÷",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action('/')).grid(row=1, column=3)

            Button(calc_frame,text="%",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.action('%')).grid(row=4, column=2)

            Button(calc_frame,text="7",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action('7')).grid(row=1, column=0, padx=5)

            Button(calc_frame,text="8",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.action(8)).grid(row=1, column=1)

            Button(calc_frame,text="9",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action(9)).grid(row=1, column=2)

            Button(calc_frame,text="4",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.action(4)).grid(row=2, column=0, padx=5)

            Button(calc_frame,text="5",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action(5)).grid(row=2, column=1, sticky=W)

            Button(calc_frame,text="6",width=5,height=3,
                   fg="white",bg="blue",
                   command=lambda:self.action(6)).grid(row=2, column=2)

            Button(calc_frame,text="1",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.action(1)).grid(row=3, column=0, padx=5)

            Button(calc_frame,text="2",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action(2)).grid(row=3, column=1)

            Button(calc_frame,text="3",width=5,height=3,
                   fg="white",bg="blue",
                   command=lambda:self.action(3)).grid(row=3, column=2)

            Button(calc_frame,text="0",width=5,height=3,
                   fg="white",bg="blue",
                   command=lambda:self.action(0)).grid(row=4, column=0, padx=5)

            Button(calc_frame,text=".",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.action('.')).grid(row=4, column=1)

            Button(calc_frame,text="(",width=5,height=3,
                   fg="white",bg="blue",
                   command=lambda:self.action('(')).grid(row=2, column=4)

            Button(calc_frame,text=")",width=5,height=3,
                   fg="blue",bg="orange",
                   command=lambda:self.action(')')).grid(row=2, column=5)

            Button(calc_frame,text="?",width=5,height=3,
                   fg="red",bg="light green",
                   command=lambda:self.squareroot()).grid(row=3, column=4)

            Button(calc_frame,text="x²",width=5,height=3,
                   fg="white",bg="blue",
                   command=lambda:self.square()).grid(row=3, column=5)

#root = Tk()

 # object instantiated


UnitOptionList = ["kg", "gram", "Lt", "ml","unit"]
BrandOptionList = ["Dabar", "Ruchi", "Asirbad", "MDH","Everest"]


def purchase_window():
    global purchase_screen
    global calc_frame
    global vUnit
    vUnit = StringVar(master)
    vUnit.set("Unit")
    vBrand = StringVar(master)
    vBrand.set("Brand")

    #login_screen.destroy()
    purchase_screen = Toplevel(master)
    purchase_screen.title("purchase window")
    purchase_screen.geometry("900x600")

    # Header Frame:
    header_frame = Frame(purchase_screen,  bd=4, relief=RIDGE,  bg="crimson" )
    header_frame.place(x=5, y=5, width=890, height=50)
    Button(header_frame, text="Back", font=("Calibri", 12), bg="crimson").pack(side=RIGHT)
    Label(header_frame, text="Purchase Dashboard", font=("Calibri", 15, "bold"), bg="crimson").pack(fill=BOTH)

    # ENTRY FRAME:
    entry_frame = Frame(purchase_screen,  bd=4, relief=RIDGE,  bg="crimson" )
    entry_frame.place(x=5, y=55, width=342, height=540)
    #Label
    Label(entry_frame, text="Date", font=("Calibri", 12), bg="crimson").grid(row=0, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Item", font=("Calibri", 12), bg="crimson").grid(row=1, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Quantity", font=("Calibri", 12), bg="crimson").grid(row=2, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Unit price", font=("Calibri", 12), bg="crimson").grid(row=3, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Sale price", font=("Calibri", 12), bg="crimson").grid(row=4, column=0, padx=5, pady=5, sticky=W)

    #Entry
    txt_date = DateEntry(entry_frame, width=23, background='darkblue',foreground='white', borderwidth=2)
    txt_date.grid(row=0, column=1, pady=5, padx=5, sticky=W)
    txt_item = Entry(entry_frame, width=20, font=("Calibri", 12))
    txt_item.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    brand = OptionMenu(entry_frame, vBrand, *BrandOptionList)
    brand.config(width=7, font=('Helvetica', 7))
    brand.grid(row=1, column=2, padx=2, pady=5, sticky=W)


    txt_qty = Entry(entry_frame, width=20, font=("Calibri", 12))
    txt_qty.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    unit = OptionMenu(entry_frame, vUnit, *UnitOptionList)
    unit.config(width=7, font=('Helvetica', 7))
    unit.grid(row=2, column=2, padx=2, pady=5, sticky=W)

    txt_unit_price = Entry(entry_frame, width=20, font=("Calibri", 12))
    txt_unit_price.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    txt_sale_price = Entry(entry_frame, width=20, font=("Calibri", 12))
    txt_sale_price.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    # BUTTON FRAME ENTRY:
    button_frame = Frame(entry_frame,  bd=4, relief=RIDGE,  bg="yellow" )
    button_frame.place(x=1, y=200, width=331, height=45)
    #Button:
    add_btn = Button(button_frame, text="Add", width=7)
    add_btn.grid(row=0, column=0, padx=3, pady=5, sticky=W)
    update_btn = Button(button_frame, text="Update", width=10)
    update_btn.grid(row=0, column=1, padx=3, pady=5, sticky=W)
    delete_btn = Button(button_frame, text="Delete", width=10)
    delete_btn.grid(row=0, column=2, padx=3, pady=5, sticky=W)
    clear_btn = Button(button_frame, text="Clear", width=10)
    clear_btn.grid(row=0, column=3, padx=3, pady=5, sticky=W)

    # Calculator frame
    calc_frame = Frame(entry_frame,  bd=4, relief=RIDGE,  bg="crimson" )
    calc_frame.place(x=1, y=246, width=331, height=285)
    obj=calc(calc_frame)

    # DETAIL FRAME:
    detail_frame = Frame(purchase_screen,  bd=4, relief=RIDGE,  bg="crimson" )
    detail_frame.place(x=350, y=55, width=545, height=540)
    # SEARCH FRAME DETAILS
    search_frame = Frame(detail_frame,  bd=4, relief=RIDGE,  bg="yellow" )
    search_frame.place(x=1, y=1, width=535, height=35)

    Button(search_frame, text="Search", width=15).grid(row=0, column=0, sticky=W)
    Button(search_frame, text="Submit", width=15).grid(row=0, column=2, sticky=W, padx=26)
    txt_search = Entry(search_frame, width=32, font=("Calibri", 12))
    txt_search.grid(row=0, column=1, sticky=W, padx=5)


master = Tk()
master.geometry('300x300')

purchase_window()

#you can make as many Toplevels as you like

master.mainloop()
