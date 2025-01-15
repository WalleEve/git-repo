# Tkinter Sizegrip

# The Sizegrip widget typically locates in the bottom right corner of the window.
# It allows us to resize the enter application window.

# To create a Sizegrip widget, we use the following syntax:
# ttk.Sizegrip(parent, **option)

# To make sure the Sizegrip widget works properly, we need to make the root window resizable.

# If we use the grid geometry manager, we need to configure column and row sizes.

# Tkinter Sizegrip widget example:
# The following program display a Sizegrip at the bottom right of the root window:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sizegrip Demo")
root.geometry("300x200")
root.resizable(True, True)

# grid layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create the sizegrip
sg = ttk.Sizegrip(root)
sg.grid(row=1, sticky=tk.SE)

root.mainloop()
