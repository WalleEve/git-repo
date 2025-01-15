# Python programm to
# Illustrate Separator
# widget


# Import required modules
from tkinter import *
from tkinter import ttk


# Main tkinter window
x = Tk()
x.geometry("400x300")


# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.4)


# Seperator object
#separator = ttk.Separator(x, orient='vertical')
#separator.place(relx=0.47, rely=0, relwidth=0.2, relheight=1)

# Seperator object
#separator = ttk.Separator(x, orient='horizontal')
#separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)


# Label Widget
#a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Seperator")
#a.place(relx=0.5, rely=0.1, relheight=0.8, relwidth=0.4)


mainloop()

"""

# Python programm to
# Illustrate Separator
# widget


# Import required modules
from tkinter import *
from tkinter import ttk


# Main tkinter window
x = Tk()
x.geometry("400x300")


# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.1, rely=0.05, relheight=0.4, relwidth=0.8)


# Seperator object
separator = ttk.Separator(x, orient='horizontal')
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)


# Label Widget
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Seperator")
a.place(relx=0.1, rely=0.5, relheight=0.4, relwidth=0.8)


mainloop()
"""
