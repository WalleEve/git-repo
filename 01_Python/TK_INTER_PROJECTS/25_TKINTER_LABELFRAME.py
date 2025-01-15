# Tkinter LabelFrme

# Tkinter LabelFrame widget is a container that contains other related widgets. For example we can group rediobutton widgets and place the group on a LabelFrame.

# To create a LabelFrame widget, we use the ttk.LabelFrame:

# lf = ttk.LabelFrame(container, **options)

## Tkinter LabelFrame widget Example:
# The following program illustrate how to create a LabelFrame widget that groups three radio buttons:

import tkinter as tk
from tkinter import ttk


# root window
root  = tk.Tk()

# Configure the root window
root.geometry("300x200")
root.resizable(False, False)
root.title("LabelFrame Demo")

# Label Frame
lf = ttk.LabelFrame(root, text="Alignment")
lf.grid(column=0, row=0, padx=20, pady=20)

alignment_var = tk.StringVar()
alignments = ('Left', 'Center', 'Right')

# create radio buttons and place them on the label frame

grid_column=0

for alignment in alignments:
    # creae a radio button
    radio = ttk.Radiobutton(lf, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

root.mainloop()


# Specify the label position
# To specify the position of the label on the widget, we use the labelanchor option.
# The labelanchor defaults to 'nw' which places the label at the left and of the top border
"""
_______ nw ___ n ___ ne ____
|                           |
|                           |
wn                         en
|                           |
w                           e
|                           |
ws                          es
|                           |
|______ sw ____ s ___ se ___|

"""


# The following program illustratr the label anchor options.
# When we select a label option, the label of the LabelFrame widget change accordingly

import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.title("LabelFrame Label Anchor")

# Label Frame
lf = ttk.LabelFrame(root, text="Label Anchor")
lf.grid(column=0, row=0, padx=20, pady=20, sticky=tk.NSEW)

anchor_var = tk.StringVar()
anchors = {
'nw': {'row': 0, 'column': 1},
'n': {'row': 0, 'column': 2},
'ne': {'row': 0, 'column': 3},
'en': {'row': 1, 'column': 4},
'e': {'row': 2, 'column': 4},
'es': {'row': 3, 'column': 4},
'se': {'row': 4, 'column': 3},
's': {'row': 4, 'column': 2},
'sw': {'row': 4, 'column': 1},
'ws': {'row': 3, 'column': 0},
'w': {'row': 2, 'column': 0},
'wn': {'row': 1, 'column': 0}
}

def change_label_anchor():
    lf['labelanchor'] = anchor_var.get()

# create radoi buttons and place them on the label frame
for key, value in anchors.items():
    # create a radoi button
    radio = ttk.Radiobutton(
    lf,
    text=key.upper(),
    value=key,
    command = change_label_anchor,
    variable = anchor_var
    ).grid(**value, padx=10, pady=10, sticky=tk.NSEW)

# set the radoi button selected
anchor_var.set(lf['labelanchor'])

root.mainloop()
