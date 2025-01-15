## Tkinter Listbox

# A listbox widget displays a list of single line items.
# A Listbox allows us to browse throuse the items and select one or multiple items at once

# To create a listbox, we use the tk.Listbox class

# listbox = tk.Listbox(container, listvariable, height)

# The container is the parent component of the listbox
# The listvariable links to a StringVar object.
# The height is the number of items that the Listbox will display without scrolling.


## Managing List Items
# To populate items to a Listbox, we first create a StringVar object
# That is initialized with a list of items.
# Then we assign this StringVar object to the listvariable option
"""

list_item = StringVar(value=items)
listbox = tk.Listbox(
container,
height,
listvariable=list_item
)
"""
# To add, remove, or rearrange items in the Listbox, we just need to modify the list_items variable.

## Selecting List Items
# The selectmode option determines whether we can select a single or multiple items at a time.

# . 'browse'  - allows a single selection
# . 'exteded' - allows multiple selection.

# By default, the selectmode is 'browse'. The curselection() method returns a list of currently selected indices.

## Binding the Selected Event:

# To execute a function when the selected items changes, we bind that function to the <<ListboxSelect>> event.

# listbox.bind('<<ListboxSelect>>', callback)

# Tkinter Listbox widget Example:

# The following program display a Listbox that contains a list of programming languages.

# When we select one or more items, the program displays the selected ones on a message box.

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# create the root window
root = tk.Tk()
root.geometry('200x200')
root.resizable(False, False)
root.title("Listbox")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a list box
langs = ('Java', 'C#', 'C', 'C++', 'Python', 'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)

listbox = tk.Listbox(
root,
listvariable = langs_var,
height=6,
selectmode='extended'
)

listbox.grid(column=0, row=0, sticky='nwes')

# handel event
def items_selected(event):
    """
        handle item selected event
    """
    # get the selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_items = ','.join([listbox.get(i) for i in selected_indices])
    msg = f" You selected {selected_items}"

    showinfo(title="Information", message=msg)

listbox.bind("<<ListboxSelect>>", items_selected)


root.mainloop()

"""
How it works.

First, create a StringVar that holds a list of programming languages:

langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

langs_var = tk.StringVar(value=langs)
Code language: Python (python)

Second, create a new Listbox widget and assign the StringVar object to the listvariable:

listbox = tk.Listbox(
    root,
    listvariable=langs_var,
    height=6,
    selectmode='extended')
Code language: Python (python)

The height shows six programming languages without scrolling. The selectmode='extended' allows multiple selections.

Third, define a function that will be invoked when one or more items are selected. The items_selected() function shows a list of currently selected list items:

def items_selected(event):
    """ #handle item selected event
    """
    # get selected indices
    selected_indices = listbox.curselection()
    # get selected items
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(
        title='Information',
        message=msg)
Code language: Python (python)

Finally, bind the items_selected function with the '<<ListboxSelect>>' event:

listbox.bind('<<ListboxSelect>>', items_selected)
"""

# Adding a scrollbar to the Listbox:

# The following program illustrates how to add a scrollbar to a listbox:

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

listbox.bind(''<<ListboxSelect>>, item_selected)

root.mainloop()
