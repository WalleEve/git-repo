import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.geometry('200x100')
root.resizable(False, False)
root.title('Listbox')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value = langs)

listbox = tk.Listbox(
root,
listvariable=langs_var,
height=6,
selectmode='extended'
)

listbox.grid(
column=0,
row=0,
sticky='nwes'
)

# link a scrollbar to a list:
scrollbar = ttk.Scrollbar(root, orient='vertical', command=listbox.yview)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.grid(column=1, row=0, sticky='ns')

# handle event
def item_selected(event):
    """
    handle item selected event
    """

    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ','.join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(title = "Information", message=msg)

listbox.bind('<<ListboxSelect>>', item_selected)

root.mainloop()


""""
Summary

    Use the tk.Listbox(container, height, listvariable) to create a Listbox widget; a listvariable should be a tk.StringVar(value=items).
    Set the selectmode to 'extended' to allow multiple selection; otherwise, use 'browse'.
    Bind a callback function to the '<>' event to execute the function when one or more list items are selected.
"""
