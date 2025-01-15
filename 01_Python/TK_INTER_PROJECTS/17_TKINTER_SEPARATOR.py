## Tkinter Separator

# A separator widget placed a thin horizontal or vertical rule between groups of widgets.

# To create a separator widget, we use the ttk.Separator constructor

# sep = ttk.Separator(container, orient="horizontal")

# The orient option can be either "horizontal" or "vertical"

# The following example illustrates how to use a separator widget to separate two labels:

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Separator Widget Demo")

ttk.Label(root, text="First Label").pack()
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill='x')
ttk.Label(root, text="Second Label").pack()
vseparator = ttk.Separator(root, orient="vertical")
vseparator.pack(fill='y', expand=True)

root.mainloop()


# Notice that the size of a separator is 1px. Therefore we need to se the fill or sticky property to adjust its size.
