## Tkinter Combobox

# A combobox is a combnation of an Entry widget and a Listbox widget.
# A combobox widget allows us to select one value in a set of values. In addition it allows us to enter a custom value.

## Create a combobox

#To Create a combobox widget, we will use the ttk.Combobox() constructor.

# current_var = tk.StringVar()
# combobox = ttk.combobox(container, textvaribale=current_var)

# The container is the window or frame on which we want to place the combobox widget.

# The textvariable argument links a variable current_var to the current value of the combobox

# To get the current selected value, we can use the current_var variable

# current_value = current_var.get()

# Alternet, we can use the get() method of the combobox object:

# current_value = combobox.get()

# To set the current value, we use the current_var variable or the set() method of the combobox object

# current_value.set(new_value)
# combobox.set(new_value)

## Define Value set:

# The combobox has the values property that we can assign a list of values to it like:
# combobox['values'] = ('value1', 'value2', 'value3')

# By default we can enter a custom value in the combobox. If we do not want this we can se the state option to 'readonly'

# combobox['state'] = 'readonly'

# To re-enable the combobox, we use the 'normal' state like:
# combobox['state'] ='normal'

## BIND EVENT:
# When a select value changes, the combobox widget generate a '<<ComboboxSelected>>' virtual event. To handel the event, we can use the bond() method

# combobox.bind('<<ComboboxSelected>>', callback)

# The callback will execute when the selected value of the combobox changes.

## Set the current Value:

# To set the current value, we use the set() method

# combobox.set(self, value)

# also we can use the current() method

# current(self, newindex=None)

# The newindex specifies the index of values from the list that we want to select as the current value.

# If we do not specify the index of values rom the list that we want to select as the current value or -1 if the current value doesn't sppear in the list

## Python Tkinter combobox example:

# The following program illustrate how to create a combobox widget.
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


root = tk.Tk()

# config the root window
root.geometry("300x200")
root.resizable(False, False)
root.title("Combobox Widget")

# label
label = ttk.Label(text="Please Select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)

# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
    title="Result",
    message=f"You selected {selected_month.get()}"
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()



# The following program shows the same month combobox widget and uses the set() method to set the current value to the current month:

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

root = tk.Tk()

# config the root window

root.geometry("300x200")
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letter of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)

# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
    title="Result",
    message=f"You selected {selected_month.get()}"
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)

# Set the current month
current_month = datetime.now().strftime('%b')
month_cb.set(current_month)

root.mainloop()


"""
Summary

    Use ttk.Combobox(root, textvariable) to create a combobox.
    Set the state property to readonly to prevent users from entering custom values.
    A combobox widget emits the '<<ComboboxSelected>>' event when the selected value changes.

"""
