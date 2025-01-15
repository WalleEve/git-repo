## Tkinter Radio Button

# Radio buttons allows us to select between one of a number of mutually exclusive choise.
# Typically, we use radio buttons together in a set.
# Theya are a good option if we have a few choices that we want users to select.

# To create a radio buttons,we use the Radiobutton widget.
"""

selected = tk.StringVar()
r1 = ttk.Radiobutton(container, text='Option 1', value='Value 1', variable=selected)
r2 = ttk.Radiobutton(container, text="Option 2", value="Value 2", variable=selected)
r3 = ttk.Radiobutton(container, text="Option 3", value="Value 3", variable=selected)

"""

# Each radio button has a different value.
# Radio buttons in the same group shares the same variable.

# The container is the parent widget which we place the radio buttons on.
# The text argument specifies the text that appears on the radio button.
# The value argument specifies the value that the radio button will hold.
# The variable must be a tk.StringVar()



## Tkinter radio button example:
# The following program illustrate how to use radio buttons. It returns the selected size once we click the Get Selected Size button.

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# root window

root = tk.Tk()
root.geometry("300x250")
root.resizable(False, False)
root.title("Radio Button Demo")

def show_selected_size():
    showinfo(title="Result", message=selected_size.get())

selected_size = tk.StringVar()

sizes = (('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra Large', 'XL'),
    ('Extra Extra Large', 'XXL'))

label = ttk.Label(root, text="What is your t-shirt size?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# Button
button = ttk.Button(
    root,
    text="Get selected Size",
    command=show_selected_size
)
button.pack(fill='x', padx=5, pady=5)


root.mainloop()

"""
Summary

    Use ttk.Radiobutton(text, variable) to create a radio button; the variable should be a tk.StringVar()
    A set of radio buttons share the same variable.
"""
