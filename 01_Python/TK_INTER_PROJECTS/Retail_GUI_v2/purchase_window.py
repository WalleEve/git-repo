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

# FUNCTION:

def fetch_detail_pse():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("select id, Initcap(item) item, initcap(brand) brand,  quantity, initcap(unit) unit,  unit_price,  sale_price   from current_purchase")
    rows = cur.fetchall()
    if len(rows) !=0:
        detail_table.delete(*detail_table.get_children())
        for row in rows:
            detail_table.insert('',END, values=row)
    else:
        print("No Record in current_sale table.")
    conn.commit()
    conn.close()

def get_cursor(ev):
    cursor_row = detail_table.focus()
    contents = detail_table.item(cursor_row)
    row = contents["values"]
    vtxt_item.set(row[1])
    vBrand.set(row[2])
    vtxt_qty.set(row[3])
    vUnit.set(row[4])
    vtxt_unit_price.set(row[5])
    vtxt_sale_price.set(row[6])


def purchase_search():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    vitem = vsearch_text.get()
    cur.execute(f"select id, Initcap(item), initcap(brand), quantity, unit,  unit_price, sale_price  from current_purchase where lower(item) = lower('{vitem}')")
    rows = cur.fetchall()
    if len(rows) !=0:
        for row in rows:
            vtxt_item.set(row[1])
            vBrand.set(row[2])
            vtxt_qty.set(row[3])
            vUnit.set(row[4])
            vtxt_unit_price.set(row[5])
            vtxt_sale_price.set(row[6])
    else:
        messagebox.showinfo("Record not found!")
    conn.commit()
    conn.close()

def purchase_clear():
    vtxt_item.set("")
    vBrand.set("Brand")
    vtxt_qty.set("")
    vUnit.set("Unit")
    vtxt_unit_price.set("")
    vtxt_sale_price.set("")


def purchase_add():
    temp_date = txt_date.get()
    temp_item = vtxt_item.get()
    temp_brand = vBrand.get()
    temp_quantity = vtxt_qty.get()
    temp_unit = vUnit.get()
    temp_unit_price = vtxt_unit_price.get()
    temp_sale_price = vtxt_sale_price.get()
    if temp_date =='' or temp_item == '' or temp_quantity =='' or temp_unit_price =='' or temp_sale_price =='' :
        messagebox.showerror("Error", "All feilds are reqired!")
    else:
        conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("insert into current_purchase (purchase_date, item, brand, quantity, unit, unit_price, sale_price) values(to_date( %s ,'MM/DD/YY'), upper(%s), upper(%s), %s::numeric, upper(%s), %s::numeric, %s::numeric)", (temp_date, temp_item, temp_brand,  temp_quantity, temp_unit, temp_unit_price, temp_sale_price))
    conn.commit()
    fetch_detail_pse()
    purchase_clear()
    conn.close()


def purchase_update():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("update current_purchase   set brand=%s, quantity=%s, unit=%s, unit_price=%s, sale_price=%s where initcap(item) = initcap(%s) ", (
    vBrand.get(),
    vtxt_qty.get(),
    vUnit.get(),
    vtxt_unit_price.get(),
    vtxt_sale_price.get(),
    vtxt_item.get()

    ))
    conn.commit()
    fetch_detail_pse()
    purchase_clear()
    conn.close()

def purchase_delete():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    vitem = vtxt_item.get()
    print(vitem)
    cur.execute(f"Delete from current_purchase where upper(item) = upper('{vitem}')")
    conn.commit()
    fetch_detail_pse()
    purchase_clear()
    conn.close()


def purchase_submit():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("insert into purchase_master (purchase_date, item, brand, quantity, unit, unit_price, sale_price) select purchase_date, item, brand, quantity, unit, unit_price, sale_price  from  current_purchase")
    cur.execute("truncate table current_purchase")
    detail_table.delete(*detail_table.get_children())
    conn.commit()
    #fetch_detail()
    purchase_clear()
    conn.close()
#======================================================================================================================================================
#|
#|
#|
#======================================================================================================================================================

UnitOptionList = ["kg", "gram", "Lt", "ml","unit"]
BrandOptionList = ["Dabar", "Ruchi", "Asirbad", "MDH","Everest"]


def purchase_window():
    global purchase_screen
    global calc_frame
    global detail_table
    global vUnit
    global vBrand
    global vtxt_item
    global vtxt_qty
    global vtxt_unit_price
    global vtxt_sale_price
    global vsearch_text
    global txt_date


    vtxt_item = StringVar()
    vtxt_qty =  StringVar()
    vtxt_unit_price = StringVar()
    vtxt_sale_price = StringVar()
    vsearch_text = StringVar()


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

    txt_item = Entry(entry_frame, textvariable=vtxt_item, width=20, font=("Calibri", 12))
    txt_item.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    brand = OptionMenu(entry_frame, vBrand, *BrandOptionList)
    brand.config(width=7, font=('Helvetica', 7))
    brand.grid(row=1, column=2, padx=2, pady=5, sticky=W)


    txt_qty = Entry(entry_frame, textvariable=vtxt_qty, width=20, font=("Calibri", 12))
    txt_qty.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    unit = OptionMenu(entry_frame, vUnit, *UnitOptionList)
    unit.config(width=7, font=('Helvetica', 7))
    unit.grid(row=2, column=2, padx=2, pady=5, sticky=W)

    txt_unit_price = Entry(entry_frame, textvariable=vtxt_unit_price,  width=20, font=("Calibri", 12))
    txt_unit_price.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    txt_sale_price = Entry(entry_frame, textvariable=vtxt_sale_price , width=20, font=("Calibri", 12))
    txt_sale_price.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    # BUTTON FRAME ENTRY:
    button_frame = Frame(entry_frame,  bd=4, relief=RIDGE,  bg="yellow" )
    button_frame.place(x=1, y=200, width=331, height=45)
    #Button:
    add_btn = Button(button_frame, text="Add", width=7, command=purchase_add)
    add_btn.grid(row=0, column=0, padx=3, pady=5, sticky=W)
    update_btn = Button(button_frame, text="Update", width=10, command=purchase_update)
    update_btn.grid(row=0, column=1, padx=3, pady=5, sticky=W)
    delete_btn = Button(button_frame, text="Delete", width=10, command=purchase_delete)
    delete_btn.grid(row=0, column=2, padx=3, pady=5, sticky=W)
    clear_btn = Button(button_frame, text="Clear", width=10, command=purchase_clear)
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

    Button(search_frame, text="Search", width=15, command=purchase_search).grid(row=0, column=0, sticky=W)
    Button(search_frame, text="Submit", width=15, command=purchase_submit).grid(row=0, column=2, sticky=W, padx=26)
    txt_search = Entry(search_frame, textvariable= vsearch_text, width=32, font=("Calibri", 12))
    txt_search.grid(row=0, column=1, sticky=W, padx=5)

    #DETAIL FRAME
    vale_frame = Frame(detail_frame,  bd=4, relief=RIDGE,  bg="crimson")
    vale_frame.place(x=1, y=37, width=535, height=490)

    scroll_x = Scrollbar(vale_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(vale_frame, orient=VERTICAL)

    detail_table = ttk.Treeview(vale_frame, columns=("SrNo", "Item", "Brand", "quantity",  "unit", "unit_price",  "sale_price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=detail_table.xview)
    scroll_y.config(command=detail_table.yview)

    detail_table.heading("SrNo", text="Serial")
    detail_table.heading("Item", text="Item")
    detail_table.heading("Brand", text="Brand")
    detail_table.heading("quantity", text="Quantity")
    detail_table.heading("unit", text="Unit")
    detail_table.heading("unit_price", text="Unit Price")
    detail_table.heading("sale_price", text="Sale Price")
    detail_table['show']="headings"
    detail_table.column("SrNo", width=50)
    detail_table.column("Item", width=100)
    detail_table.column("Brand", width=100)
    detail_table.column("quantity", width=100)
    detail_table.column("unit", width=50)
    detail_table.column("unit_price", width=100)
    detail_table.column("sale_price", width=100)
    detail_table.pack(fill=BOTH, expand=1)
    detail_table.bind("<ButtonRelease-1>", get_cursor)
    fetch_detail_pse()


master = Tk()
master.geometry('300x300')

purchase_window()

#you can make as many Toplevels as you like

master.mainloop()
