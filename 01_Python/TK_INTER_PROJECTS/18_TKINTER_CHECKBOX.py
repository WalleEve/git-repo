## TKINTER CHECKBOX:

# A checkbox is a widget that allows us to check and uncheck
# A checkbox can hold a value and invoke a callback it's checked or unchecked.
# Typically, we use a checkbox when we want to ask users to choose between two values.
# To create a checkbox, we use the ttk.Checkbutton constructor.

"""
checkbox_var = tk.StringVar()

def check_changed():
    pass

checkbox = ttk.Checkbutton(container,
    text='<checkbox label>',
    command = check_changed,
    variable=checkbox_var,
    onvalue='<value_when_checked>',
    offvalue='<value_when_unchecked>')
"""

# The container argument specifies the window that we want to place the checkbox.
# The text argument specifies the label for the checkbox
# The command is a callable that will be called once the checkbox is checked or unchecked.
# The variable holds the current value of the checkbox. If the checkbox is checked, the value of the variable is 1. Otherwise it is 0
# if we want other values then 0 and 1, we can speficy them in the onvalue and offvalue optons
# If the linked variable doesn't exits, or its value is neither the on  or off value, the checkbox is in the indeterminate or tristate mode.

# Tkinter checkbox example:
# The following program illustrate how to use a checkbox widget. Once we check or uncheck the checkbox, a message box will show the on value and the off value accordingly.

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Checkbox Demo")

agreement = tk.StringVar()

def agreement_changed():
    tk.messagebox.showinfo(title="Result", message=agreement.get())

ttk.Checkbutton(root,
    text="I agree",
    command=agreement_changed,
    variable=agreement,
    onvalue="agree",
    offvalue="disagree").pack()

root.mainloop()


"""
Summary

    Use ttk.Checkbutton(text, variable) to create a checkbox; the variable is a tk.StringVar().
    Use command argument to specify a function that executes when the button is checked or unchecked.
    Use the onvalue and offvalue to determine what value the variable will take.

"""
