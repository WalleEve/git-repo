# TKINTER PACK:

# Tkinter pack geometry manager.

"""
The pack() method is used to add widget to the window

To arrange widgets on a window, we use geometry managets. The pcak() method is one of three geometry managers in tkinter. 
The othere geometry managers are grid() and place()

The pack geometry manager has many configurations. The follwing are the ost commonly used options:

fill 
expand 
side 
ipadx 
ipady 
padx 
pady

"""


# Tkinter pack geometry manager example:

# The following shows how to use the pack geometry manager to arrange two Lebel widgets on the root window.

import tkinter as tk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Pack Demo")


# box 1 

box1 = tk.Label(
root,
text="Box 1",
bg="green",
fg="white")

box1.pack(
ipadx=10,
ipady=10)

# box2 
box2 = tk.Label(
root, 
text="Box 2",
bg="red",
fg="white")

box2.pack(
ipadx=10,
ipady=10)

root.mainloop()
# https://www.pythontutorial.net/wp-content/uploads/2020/11/tkinter-pack.png
# This example used the ipadx and ipady for the internal padding. 
# These options create space between the labels and their borders.

# USING THE FILL OPTION 

# The fill option accepts three values 'x', 'y' and 'both'.
# These options allow the widget to fill availabe space along the x-axis and y-axix and both.

# if we add the fill='x'  to the first widget 
"""
box1.pack(
ipadx=10,
ipady=10,
fill='x')
"""
# We can see that the widget fills all available space scross the x-axis.

import tkinter as tk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Pack Demo")


# box 1 

box1 = tk.Label(
root,
text="Box 1",
bg="green",
fg="white")

box1.pack(
ipadx=10,
ipady=10,
fill='x')

# box2 
box2 = tk.Label(
root, 
text="Box 2",
bg="red",
fg="white")

box2.pack(
ipadx=10,
ipady=10)

root.mainloop()


# However if we change to fill='y' 
"""
box1.pack(
ipadx=10,
ipady=10,
fill='y')

"""
# we will see the the first widget doesn't fill all space vertically.
# Basically the pack geometry manager allocates space to the widget as per the available space vertically and horizontally


# https://www.pythontutorial.net/wp-content/uploads/2020/11/tkinter-pack-allocated-space.png


# USING THE EXPAND OPTION:
# The expand option allocate more available space to the widget.
# if we add the expand option to the first widget.
"""
box1.pack(
ipadx=10,
ipady=10,
expand=True)
"""
import tkinter as tk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Pack Demo")


# box 1 

box1 = tk.Label(
root,
text="Box 1",
bg="green",
fg="white")

box1.pack(
ipadx=10,
ipady=10,
expand=True)

# box2 
box2 = tk.Label(
root, 
text="Box 2",
bg="red",
fg="white")

box2.pack(
ipadx=10,
ipady=10)

root.mainloop()

# The first widget takes all the available space in the window except for the space allocate to the second widget.
# Since the first widget doesn't have the fill option, it floats in the middle of the allocated area.

# if we set fill to both:

"""
box1.pack(
ipadx=10,
ipady=10,
fill='both',
expand=True)
"""
# We will see that the first widget fills up most of the window

import tkinter as tk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Pack Demo")


# box 1 

box1 = tk.Label(
root,
text="Box 1",
bg="green",
fg="white")

box1.pack(
ipadx=10,
ipady=10,
fill='both',
expand=True)

# box2 
box2 = tk.Label(
root, 
text="Box 2",
bg="red",
fg="white")

box2.pack(
ipadx=10,
ipady=10)

root.mainloop()



# Notice that the second widget doesn't use all allocated space because it doesn't have the fill option.

# when we se the expand to True for all wigets, the pack manager will allocate space to them evenly.
# However, this is only true when all the widgets share the same anchor side.

# USING SIDE OPTION:

# The side option specifies the alignment of the widget. 
# It can be 'left', 'top', 'right', 'bottm'.

# The side default to top. 
# In other words, widgets are aligned to the top of their container.

# The following example sets the side of the first widget to 'left'

import tkinter as tk 

root = tk.Tk()
root.title("Pack Demo")
root.geometry("300x200")

# box 1
box1 = tk.Label(
root, 
text = "Box 1",
bg = "green",
fg = "white")

box1.pack(
ipadx=10,
ipady=10,
expand=True,
fill='both',
side='left')

# box 2 
box2 = tk.Label(
root,
text = "Box 2",
bg = "red",
fg = "white")

box2.pack(
ipadx=10,
ipady=10,
expand=True,
fill='both'
#side='left'
)

root.mainloop()


# In this example the expand option may not work as we expected. THe reason is that widgets have different sides.
# To make their space even again we can set the side of both widgets to 'left'
# or one is 'left' and the other is 'right'

import tkinter as tk 

root = tk.Tk()
root.title("Pack Demo")
root.geometry("300x200")
root.resizable(False, False)

# Box 1
box1 = tk.Label(
root,
text="Box 1",
bg="green",
fg="white")

box1.pack(
ipadx=10,
ipady=10,
expand=True,
fill='both',
side='left')

# Box 2
box1 = tk.Label(
root,
text="Box 2",
bg="red",
fg="white")

box1.pack(
ipadx=10,
ipady=10,
expand=True,
fill='both',
side='left')


root.mainloop()

# When to use the Pack geometry manager:

# The geometry manager is suitable for the following
# Placing widgets in a top-down layout.
# Placing widgets side by side

# Example:

import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("300x200")
root.title("Pack Demo")
root.resizable(False, False)

# place widgets top down
label1 = ttk.Label(root, text="Box 1", bg="red", fg="white")
label1.pack(ipadx=10, ipady=10, fill='x')

label2 = ttk.Label(root, text="Box 2", bg="green", fg="white")
label2.pack(ipadx=10, ipady=10, fill='x')

label3 = ttk.Label(root, text="Box 3", bg="blue", fg="white")
label3.pack(ipadx=10, ipady=10 fill='x')


root.mainloop()
