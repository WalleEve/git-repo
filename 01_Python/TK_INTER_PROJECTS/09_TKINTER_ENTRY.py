# TKINTER ENTRY WIDGET:

# The Entry widget allows us to enter a sing-line text. In Tkinter to create a textbox we use the Entry widget.

# textbox = ttk.Entry(container, **options)



 #   The container is the parent frame or window. on which you want to place the widget.
 #   The options is one or more keyword arguments used to configure the Entry widget.


# Note that if we want to enter multi-line text, we should use the Text widget.

# To get the current text of a Entry widget as a string we use the get() method.

# textbox.get()

# Typically we associate the current value of the textbox with a StringVar object.

# text = ttk.StringVar()
# textbox = ttk.Entry(root, textvariable = text)


# First create a new instance of the Stringvar calss. The text will be the value holder for a string variable.
# Second, assign the text variable to the textvariable of the Entry widget.

# We can use call the get() method of the StringVar() object to get the current value of the entry widget.

# text.get()


# Setting the focus to the tkinter Entry widget.

# To provide a beer user experience we can place the move the focus to the first Entry widget after the window appears.
# Once the Entry widget has focus, it's ready to accept the use input.

# To do it we use the focus() method of the Entry widget.

# textbox.focus()

# Showing a Tkinter password Entry.

# To hide sensitive information on the Entry widget e.g., a password we can use the sow option.

# the followng creates a password entry, When we enter a password, It doesn't show the actual characters bit the asterisks(*) specified in the show option.


"""
password = tk.StringVar()
password_entry = ttk.Entry(
    root, 
    textvariable = password,
    show = "*"
)
password_entry.pack()
"""

# Tkinter Entry Widget Example:

import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo 


# root, window 
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title("Sign In")


# store email address and password 

email = tk.StringVar()
password = tk.StringVar()

def login_clicked():
    """
    callback when the login button clicked"""

    msg = f"You enterd email: {email.get()} and password: {password.get()} "
    showinfo(
        title="Information",
        message = msg
    )


# Sign in Frame 

signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill="x", expand=True)


# email 

email_label = ttk.Label(signin, text="Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()


# password 

password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)


# login button 
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)

root.mainloop()



