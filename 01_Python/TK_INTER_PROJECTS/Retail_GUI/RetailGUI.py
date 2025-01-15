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
import psycopg2
import datetime
from tkinter import messagebox
from tkinter import ttk, Canvas
from tkcalendar import Calendar, DateEntry


# Main Screen:
master  = Tk()
master.title("Retail App")
master.geometry('230x450')
master.configure(bg="#003e53")

# Functions:

def purchase_text_clear():
    temp_date.set('')
    temp_item.set('')
    temp_qty.set('')
    temp_unit_price.set('')

# STOCK Functions:
def get_cursor(ev):
    cursor_row = retail_table.focus()
    contents = Student_table.item(cursor_row)
    row = contents["values"]
    roll_no_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    gender_var.set(row[3])
    contact_var.set(row[4])

def fetch_data():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("select to_date(p.entry_date,'dd-mon-yyyy') entry_date , upper(p.item), p.quentity, p.unit_price, p.quentity::numeric * p.unit_price::numeric total_amt from purchase p")
    rows = cur.fetchall()
    if len(rows) !=0:
        retail_table.delete(*retail_table.get_children())
        for row in rows:
            print(row)
            retail_table.insert('',END, values=row)
        conn.commit()
    conn.close()
def stock():
    global retail_table
    stock_dashboard = Toplevel(master)
    stock_dashboard.geometry("600x400")
    stock_dashboard.title("Stock Dashboard")
    # Labels
    Label(stock_dashboard, text="STOCK DASHBOARD", font=("Calibri", 15), width=30).pack(side=TOP, fill=BOTH)
    table_Frame = Frame(stock_dashboard, bd=4, relief=RIDGE,  bg="crimson")
    table_Frame.place(x=5, y=30, width=590, height=350)
    scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(table_Frame, orient=VERTICAL)

    retail_table = ttk.Treeview(table_Frame, columns=("date", "Item", "total_quantity", "unit_price", "total_price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=retail_table.xview)
    scroll_y.config(command=retail_table.yview)

    retail_table.heading("date", text="Purchase Date")
    retail_table.heading("Item", text="Item")
    retail_table.heading("total_quantity", text=" Total Quantity")
    retail_table.heading("unit_price", text="Unit Price")
    retail_table.heading("total_price", text="Total Amount")
    retail_table['show']="headings"
    retail_table.pack(fill=BOTH, expand=1)
    #retail_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()



# PURCHASE FUNCTIOS:
def submit_purchase():
    get_date = temp_date.get()
    get_item = temp_item.get()
    get_qty = temp_qty.get()
    get_unit_price = temp_unit_price.get()


    if get_date =='' or get_item  == '' or get_qty == '' or get_unit_price == '':
        messagebox.showerror("Error", "All feilds are reqired!")
    else:
        conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("insert into purchase(entry_date, item, quentity, unit_price) values(%s, %s, %s, %s )", (get_date, get_item, get_qty, get_unit_price))
    conn.commit()
    purchase_text_clear()
    messagebox.showinfo("Success", "Record insterted")



def purchase():
    global temp_date
    global temp_item
    global temp_qty
    global temp_unit_price

    temp_date = StringVar()
    temp_item = StringVar()
    temp_qty = StringVar()
    temp_unit_price = StringVar()

    purchase_dashboard = Toplevel(master)
    purchase_dashboard.title("Stock Dashboard")
    # ENTRY FRAME:
    purchase_frame = Frame(purchase_dashboard)
    purchase_frame.grid(row=2, sticky=W)

    # Labels
    Label(purchase_dashboard, text="PURCHASE DASHBOARD", font=("Calibri", 15), width=30, ).grid(row=0, sticky=N, pady=10)
    Label(purchase_dashboard, text="Purchase Entry", font=("Calibri", 13), width=30).grid(row=1, sticky=N, pady=5)


    Label(purchase_frame, text="Entry Date:", font=("Calibri", 11)).grid(row=3, sticky=W, padx=2, pady=2)
    Label(purchase_frame, text="Item:", font=("Calibri", 11)).grid(row=4, sticky=W, padx=2, pady=2)
    Label(purchase_frame, text="Total Quantity:", font=("Calibri", 11)).grid(row=5, sticky=W, padx=2, pady=2)
    Label(purchase_frame, text="Price Per Unit:", font=("Calibri", 11)).grid(row=6, sticky=W, padx=2, pady=2)
    Label(purchase_frame, text="", font=("Calibri", 11)).grid(row=9, sticky=W, padx=2, pady=2)

    # Entry
    Entry(purchase_frame, textvariable = temp_date, width=30).grid(row=3, column=1, sticky=W, padx=2, pady=2)
    Entry(purchase_frame, textvariable = temp_item, width=30).grid(row=4, column=1, sticky=W, padx=2, pady=2)
    Entry(purchase_frame, textvariable = temp_qty, width=30).grid(row=5, column=1, sticky=W, padx=2, pady=2)
    Entry(purchase_frame, textvariable = temp_unit_price, width=30).grid(row=6, column=1, sticky=W, padx=2, pady=2)
    #Entry(purchase_frame, width=30).grid(row=7, column=1, sticky=W, padx=2, pady=2)

    # BUTTON
    Button(purchase_frame, text="Submit", width=15, command=submit_purchase).grid(row=8, sticky=W, padx=2, pady=2)


# SALE:


def fetch_detail():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("select Initcap(item), quantity, unit_price,  (quantity::numeric * unit_price::numeric) total_amt   from current_sale")
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
    temp_date_var.set("")
    temp_item_var.set(row[0])
    temp_quantity_var.set(row[1])
    temp_unit_price_var.set(row[2])

def sale_clear():
    temp_date_var.set("")
    temp_item_var.set("")
    temp_quantity_var.set("")
    temp_unit_price_var.set("")

def sale_add():
    vdate = txt_date.get()
    vitem = temp_item_var.get()
    vqty = temp_quantity_var.get()
    v_uprice = temp_unit_price_var.get()
    if vdate =='' or vitem == '' or vqty =='' or v_uprice =='':
        messagebox.showerror("Error", "All feilds are reqired!")
    else:
        conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("insert into current_sale values(to_date( %s ,'MM/DD/YYYY'), %s, %s, %s)", (vdate, vitem, vqty, v_uprice))
    conn.commit()
    fetch_detail()
    sale_clear()
    conn.close()

def sale_update():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("update current_sale   set sale_date=to_date( %s ,'MM/DD/YYYY'), quantity=%s, unit_price=%s where initcap(item) = %s ", (
    txt_date.get(),
    temp_quantity_var.get(),
    temp_unit_price_var.get(),
    temp_item_var.get()
    ))
    conn.commit()
    fetch_detail()
    sale_clear()
    conn.close()

def sale_delete():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    vitem = temp_item_var.get()
    print(vitem)
    cur.execute(f"Delete from current_sale where lower(item) = lower('{vitem}')")
    conn.commit()
    fetch_detail()
    sale_clear()
    conn.close()

def sale_search():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    vitem = search_text.get()
    cur.execute(f"select Initcap(item), quantity, unit_price,  (quantity::numeric * unit_price::numeric) total_amt   from current_sale where lower(item) = lower('{vitem}')")
    rows = cur.fetchall()
    if len(rows) !=0:
        for row in rows:
            temp_item_var.set(row[0])
            temp_quantity_var.set(row[1])
            temp_unit_price_var.set(row[2])
    else:
        messagebox.showinfo("Record not found!")
    conn.commit()
    conn.close()

def sale_bill():
    conn = psycopg2.connect(host="localhost", port="5432", database="postgres", user="postgres", password="postgres")
    cur = conn.cursor()
    cur.execute("select count(*) total_item, sum((quantity::numeric * unit_price::numeric)) total_amt, case when sum((quantity::numeric * unit_price::numeric)) > 1000 then  (sum((quantity::numeric * unit_price::numeric))/100) * 8 else 0.00 end total_tax, case when  sum((quantity::numeric * unit_price::numeric)) > 3000 then (sum((quantity::numeric * unit_price::numeric))/100) * 10 else 0.00 end discount   from current_sale")
    rows = cur.fetchall()
    if len(rows) !=0:
        for i in rows:
            pamt = float(i[1]) + float(i[2]) + float(i[3])
            lbl_total_item.config(text="Total Items: " + str(i[0]))
            lbl_total_amount.config(text="Total Amount: " + str(i[1]))
            lbl_tax.config(text="Tax: " + str(i[2]))
            lbl_discount.config(text="Discount: " + str(i[3]))
            payable_amt.config(text="Payable Amount: " + str(pamt))
            cur.execute("insert into sales (ent_date, item, unit_rate, total_qty, total_amt) select sale_date, item, unit_price, quantity, (unit_price::numeric * quantity::numeric) total_amt  from  current_sale")
            cur.execute("truncate table current_sale")
            conn.commit()

    fetch_detail()
    sale_clear()
    conn.close()




def sale():
    sale_dashboard = Toplevel(master)
    sale_dashboard.title("Sale Dashboard")
    sale_dashboard.geometry("600x400+200+200")

    global temp_date_var
    global temp_item_var
    global temp_quantity_var
    global temp_unit_price_var
    global payable_amt
    global lbl_total_item
    global lbl_total_amount
    global lbl_tax
    global lbl_discount
    global search_text
    global detail_table
    global txt_date

    temp_date_var = StringVar()
    temp_item_var = StringVar()
    temp_quantity_var = StringVar()
    temp_unit_price_var = StringVar()
    search_text = StringVar()


    Label(sale_dashboard, text="SALES DASHBOARD", font=("Calibri", 12, "bold")).pack(side=TOP, fill=BOTH)
    # ENTRY FRAME
    entry_frame = Frame(sale_dashboard,  bd=4, relief=RIDGE,  bg="crimson" )
    entry_frame.place(x=5, y=30, width=270, height=360)

    # LABEL:
    Label(entry_frame, text="Date",  bg="crimson", font=("Calibri", 12, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Item",  bg="crimson", font=("Calibri", 12, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Quantity",  bg="crimson", font=("Calibri", 12, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky=W)
    Label(entry_frame, text="Unit Price",  bg="crimson", font=("Calibri", 12, "bold")).grid(row=3, column=0, padx=5, pady=5, sticky=W)

    # ENTRY:
    #txt_date = Entry(entry_frame, textvariable=temp_date_var, width=15, font=("times new roman", 13, "bold"))
    #txt_date.grid(row=0, column=1, pady=5, padx=5, sticky=W)
    txt_date = DateEntry(entry_frame, width=12, background='darkblue',foreground='white', borderwidth=2)
    txt_date.grid(row=0, column=1, pady=5, padx=5, sticky=W)
    txt_item = Entry(entry_frame, textvariable=temp_item_var, width=15, font=("times new roman", 13, "bold"))
    txt_item.grid(row=1, column=1, pady=5, padx=5, sticky=W)
    txt_quantity = Entry(entry_frame, textvariable=temp_quantity_var, width=15, font=("times new roman", 13, "bold"))
    txt_quantity.grid(row=2, column=1, pady=5, padx=5, sticky=W)
    txt_unit_price = Entry(entry_frame, textvariable=temp_unit_price_var, width=15, font=("times new roman", 13, "bold"))
    txt_unit_price.grid(row=3, column=1, pady=5, padx=5, sticky=W)
    # BUTTON FRAME:
    button_frame = Frame(entry_frame,  bd=4, relief=RIDGE,  bg="crimson" )
    button_frame.place(x=1, y=150, width=259, height=50)

    btn_bill = Button(button_frame, text="Add", width=6, command=sale_add)
    btn_bill.grid(row=0, column=0, padx=3, pady=5, sticky=W)
    btn_update = Button(button_frame, text="Update", width=7, command=sale_update)
    btn_update.grid(row=0, column=1, padx=3, pady=5, sticky=W)
    btn_delete = Button(button_frame, text="Delete", width=7, command=sale_delete)
    btn_delete.grid(row=0, column=3, padx=3, pady=5, sticky=W)
    btn_delete = Button(button_frame, text="Clear", width=7, command=sale_clear)
    btn_delete.grid(row=0, column=4, padx=2, pady=5, sticky=W)

    # REPORT FRAME
    report_frame = Frame(entry_frame,  bd=4, relief=RIDGE,  bg="white" )
    report_frame.place(x=1, y=210, width=259, height=140)

    lbl_total_item = Label(report_frame, text = "Total Items:",  bg="white")
    lbl_total_item.grid(row=0, column=0, padx=2, pady=0, sticky=W)
    lbl_total_amount = Label(report_frame, text = "Total Amount:",  bg="white")
    lbl_total_amount.grid(row=1, column=0, padx=2, pady=0, sticky=W)
    lbl_tax = Label(report_frame, text = "Tax:",  bg="white")
    lbl_tax.grid(row=3, column=0, padx=2, pady=0, sticky=W)
    lbl_discount = Label(report_frame, text = "Discount:",  bg="white")
    lbl_discount.grid(row=4, column=0, padx=2, pady=0, sticky=W)

    # LINE FRAME:
    line_frame = Frame(report_frame, bd=0, bg="white")
    line_frame.place(x=1, y=80, width=248, height=10)
    canvas = Canvas(line_frame,  bg="white")
    canvas.create_line(5, 5, 240, 5, dash=(4, 2))
    canvas.pack(fill=BOTH, expand=1)

    # RESULT FRAME:
    result_frame = Frame(report_frame, bd=0, bg="yellow")
    result_frame.place(x=1, y=90, width=248, height=40)
    payable_amt = Label(result_frame, text="Payable Amount:", font=("Calibri", 12), bg="Yellow")
    payable_amt.pack(side=LEFT)

    # SEARCH_FRAME
    search_frame = Frame(sale_dashboard,  bd=4, relief=RIDGE,  bg="crimson")
    search_frame.place(x=280, y=30, width=315, height=50)
    Button(search_frame, text="search", command=sale_search).grid(row=0, column=0, sticky=W)
    Button(search_frame, text="Bill", width=10, command=sale_bill).grid(row=0, column=2, sticky=W, padx=5)
    txt_search = Entry(search_frame, textvariable=search_text, width=20, font=("Calibri", 12))
    txt_search.grid(row=0, column=1, sticky=W, padx=5)


    #DETAIL FRAME
    detail_frame = Frame(sale_dashboard,  bd=4, relief=RIDGE,  bg="crimson")
    detail_frame.place(x=280, y=80, width=315, height=310)

    scroll_x = Scrollbar(detail_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(detail_frame, orient=VERTICAL)

    detail_table = ttk.Treeview(detail_frame, columns=("Item", "quantity", "unit_price", "total_price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=detail_table.xview)
    scroll_y.config(command=detail_table.yview)

    detail_table.heading("Item", text="Item")
    detail_table.heading("quantity", text="Quantity")
    detail_table.heading("unit_price", text="Unit Price")
    detail_table.heading("total_price", text="Total Amount")
    detail_table['show']="headings"
    detail_table.column("Item", width=100)
    detail_table.column("quantity", width=100)
    detail_table.column("unit_price", width=100)
    detail_table.column("total_price", width=100)
    detail_table.pack(fill=BOTH, expand=1)
    detail_table.bind("<ButtonRelease-1>", get_cursor)

def admin():
    pass



def login():
    login_name = t_uname.get()
    login_password = t_pwd.get()

    conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)
    print ("Opened database successfully");
    cursor = conn.cursor()
    cursor.execute('''SELECT user_name, password from users''')
    data = cursor.fetchall()
    for name in data:
        print(login_name, login_password )
        if name[0] == login_name and name[1] == login_password:
            login_notif.config(fg="red", text="")

            store_dashboard = Toplevel(master)
            store_dashboard.title("Dashboard")

            # Labels
            Label(store_dashboard, text="STORE DASHBOARD", font=("Calibri", 12)).grid(row=0, sticky=N, pady=10)
            Label(store_dashboard, text="Welcome to Store Management", font=("Calibri", 12)).grid(row=1, sticky=N, pady=5)

            # Buttons:
            Button(store_dashboard, text="STOCK", font=("Calibri", 12), width=30, command=stock).grid(row=2, sticky=N, padx=10, pady=5)
            Button(store_dashboard, text="PURCHASE", font=("Calibri", 12), width=30, command=purchase).grid(row=3, sticky=N, padx=10, pady=5)
            Button(store_dashboard, text="SALE", font=("Calibri", 12), width=30, command=sale).grid(row=4, sticky=N, padx=10, pady=5)
            Button(store_dashboard, text="ADMIN", font=("Calibri", 12), width=30, command=admin).grid(row=5, sticky=N, padx=10, pady=5)
        else:
            login_notif.config(fg="red", text="username or password incorrect")
            return








# Import image
img = Image.open("store.jpg")
img = img.resize((200, 200))
img = ImageTk.PhotoImage(img)



# Labels:
Label(master, text = "General Retail Store.", font = ("Calibri", 14)).grid(row=0, sticky=N, pady=10)
Label(master, text = "World Famous Store Keeper", font = ("Calibri", 12)).grid(row=1, sticky=N)
Label(master, image=img).grid(row=2, sticky=N,padx=10, pady=15)


# ENTRY FRAME:
global login_notif
btn_frame = Frame(master, width= 80, height = 40, bg= "#003e53")
btn_frame.grid()
# Label
uname = Label(btn_frame, text="User Name: ", fg="white", bg="#003e53", font=("Calibri", 10))
uname.grid(row=4, column=0, sticky=W, pady=2)
pwd = Label(btn_frame, text="Password: ", fg="white", bg="#003e53", font=("Calibri", 10))
pwd.grid(row=5, column=0, sticky=W, pady=2)
login_notif = Label(master,  bg="#003e53", font=("Calibri", 12))
login_notif.grid(row=7, column=0, sticky=W)
# Entry Box:
global temp_login_name
global temp_login_password
temp_login_name = StringVar()
temp_login_password = StringVar()
t_uname = Entry(btn_frame, textvariable = temp_login_name)
t_uname.grid(row=4, column=1, sticky=W, pady=2)
t_pwd = Entry(btn_frame, textvariable = temp_login_password)
t_pwd.grid(row=5, column=1, sticky=W, pady=2)
# Button:
log = Button(btn_frame, text="Login", width=10, command=login)
log.grid(row=6, sticky=W, padx=10, pady=10)




master.mainloop()
