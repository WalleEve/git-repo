# Tkinter Spinbox

# A Spinbox widget allows us to select a velue frm a set of values. The values can be a range of numbers

# A spinbox has as area for showing the current value and paire of arroheads.

# When we click the upward-pointing arrowhead, the Spinbox advance the current value to the next higher value in the sequence.
# If the current value reaches the maximum value, we can set it to the minimum value.

# On the other hand if we click the downward-pointing arrowhwad, the Spinbox advances the current value to the next lower value in the sequence.
# If the current value reaches the lowest value we can set it to the maximum value.

# Also we can enter a value directly into the Spinbox as if it were an Entry widget.

# To create a Spinbox widget, we use the ttk.Spinbox constructor.

# ttk.Spinbox(container, from_, to, textvariable, wrap)

# The container is the parent component of the Spinbox widget.
# The from_ is the minimum value.
# The to is the maximum value
# The textvariable specifies a tk.StringVar object that holds the current value the Spinbox

# The warp is a Boolean value. If warp equals true, when the current value reaches the maximum value, it's set to the lowest value if we click the upward-pointing arrowhead and vice versa.
# In case warp equals False, it set to the maximum value if we click the downward-pointing arrowhead.

# Note that the ttk.Spinbox has been available since Python 3.7

# Getting the current value

# To get the current value of the Spinbox, we can access the textvariable.

# current_value = tk.StringVar(value=0)
"""
spin_box = ttk.Spinbox(container, from_=0, to=30, textvariable=current_value, warp=True)
"""

# The current_value holds the current value of the Spinbox. and we can get it by calling the get() method

# current_value.get()

# Also we can use the get() method of the Spinbox object.

# spin_box.get()

# Execute a function

# To execute a function when the value of the Spinbox changes, we can assign that function to the command option.
"""

def value_changed():
    print(current_value.get())

current_value = tk.StringVar(value=0)

spin_box = ttk.Spinbox(container, from_, to, textvariable=current_value, command=value_changed)

"""

# Here the value_changed function will be execute automatically whenever the value of the Spinbox changes.

## Setting discrete steps

# To se a list of discrete steps for a Spinbox, we assign a tuple of discrete numbers to the value option like this:

# ttk.Spinbox(..., value=tuple,...)

# Tkinter Spinbox widget examples

# A simple Tkinter Spinbox widget example

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Spinbox Demo")

# Spinbox
current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
root,
from_=0,
to=30,
textvariable=current_value,
wrap=True
)
spin_box.pack()


root.mainloop()


# Tkinter Spinbox with discrete steps

# The following example shows how to create a Spinbox with discrete steps

import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Spinbox Demo")


# spinbox
current_value = tk.StringVar()
spin_box = ttk.Spinbox(root, from_=0, to=50, values=(0, 10, 20, 30, 40, 50), textvariable=current_value, wrap=True)
spin_box.pack()

root.mainloop()


"""

Summary

    Use ttk.Spinbox(container, **options) to create a Spinbox.
    Set wrap=True to set the current value to the minimum value when it reaches the maximum value and vice versa.

"""
