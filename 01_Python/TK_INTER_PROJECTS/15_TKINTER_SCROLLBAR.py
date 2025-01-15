# Tkinter Scrollbar

# A scrollbar allows us to view all part of another widget whose content is typically larger than the availablel space.

# Tkinter scrollbar widget is not a part of any other widgets such as Text and Listbox. instead, a scrollbar an independent widget.

# To use the scrollbar widget, we need to
# First, create a scrollbar widget
# Second, link the scrollbar with a scrollable widget.

# The following shows how to create a scrollbar widget using the ttk.Scrollbar constructor.

"""
scrollbar = ttk.Scrollbar(
container,
orient="vertical",
command=widget.yview
)
"""

# The container is the window or frame on which the scrollbar locates.
# The orient argument specifies whether the scrollbar needs to scroll horizontally or vertically
# The command argument allows the scrollbar widget to communicate with the scrollable widget.

# The scrollable widget also needs to communicate back to the scrollbar about the percentage of the entire content area that is currently visible.

# Every scrollable widget has a yscrollcommand and/or xscrollcommand options. And we can assign the scrollbar.set method to it.

# widget['yscrollcommand'] = scrollbar.set


 ## Tkinter scrollbar widget example:
 # The Text widget are one of several types of scrollable widgets.
 # The following program illistrates a simple use interface that consists of Text and Scrollbar widget.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

# apply the grid Layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# creae the text widget
text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky='ew')

# create a scrollbar widget and set its command to the text widget

scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# communicate back to the scrollbar

text['yscrollcommand'] = scrollbar.set
root.mainloop()

"""
Summary

    Create a scrollbar with ttk.Scrollbar(orient, command)
    The orient can be 'vertical' or 'horizontal'
    The command can be yview or xview property of the scrollable widget that links to the scrollbar.
    Set the yscrollcommand property of the scrollable widget so it links to the scrollbar.
    """
