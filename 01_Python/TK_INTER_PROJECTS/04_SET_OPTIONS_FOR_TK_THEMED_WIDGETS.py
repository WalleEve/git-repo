"""
When working with themed widgets, you often need to set their attributes e.g., text and image.

Tkinter allows you to set the options of a widget using one of the following ways:

    At widget creation, using keyword arguments.
    After widget creation, using a dictionary index.
    And use the config() method with keyword attributes.
"""

# USING KEYWORD ARGUMENTS WHEN CREATING THE WIDGET

# The following illustrates how to use the keyword arguments to set the text option for a label.

import tkinter as tk 
from tkinter import ttk

root = tk.Tk()

ttk.Label(root, text= "Hi, there").pack()

root.mainloop()


# USING A DICTIONARY INDEX AFTER WIDGET CREATION

# The following program shows the same label. However, it uses a dictionary index to set the text option for the Label widget.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label['text'] = "Hi, there"
label.pack()

root.mainloop()


# USING THE config() METHOD WITH KEYWORD ATTRIBUTES

# The following program illustrates how to use the config() method to set the text optiopn for the label.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label.config(text="Hi, there")
label.pack()

root.mainloop()


"""
Summary

Ttk widgets provide you with three ways to set options:

    Use keyword arguments at widget creation.
    Use a dictionary index after widget creation.
    Use the config() method with keyword attributes.
"""