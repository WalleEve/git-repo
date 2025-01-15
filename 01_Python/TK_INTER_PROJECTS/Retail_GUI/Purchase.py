# PURCHASE
from tkinter import *

master = Tk()

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
#Label(purchase_frame, text="Toal Value:", font=("Calibri", 11)).grid(row=7, sticky=W, padx=2, pady=2)

# Entry
Entry(purchase_frame, width=30).grid(row=3, column=1, sticky=W, padx=2, pady=2)
Entry(purchase_frame, width=30).grid(row=4, column=1, sticky=W, padx=2, pady=2)
Entry(purchase_frame, width=30).grid(row=5, column=1, sticky=W, padx=2, pady=2)
Entry(purchase_frame, width=30).grid(row=6, column=1, sticky=W, padx=2, pady=2)
#Entry(purchase_frame, width=30).grid(row=7, column=1, sticky=W, padx=2, pady=2)

# BUTTON 
Button(purchase_frame, text="Submit", width=15).grid(row=8, sticky=W, padx=2, pady=2)

master.mainloop()
