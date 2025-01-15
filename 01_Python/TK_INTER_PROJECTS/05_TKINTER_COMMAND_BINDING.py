"""
Introduction to Tkinter command binding

To make the application more interactive, the widgets need to respond to the events such as:

    Mouse clicks
    Key presses

This requires assigning a callback function to a specific event. When the event occurs, the callback will be invoked automatically to handle the event.

In Tkinter, some widgets allow you to associate a callback function with an event using the command binding.

It means that you can assign the name of a function to the command option of the widget so that when the event occurs on the widget, the function will be called automatically.

To use the command binding, you follow these steps:

    First, define a function as a callback.
    Then, assign the name of the function to the command option of the widget.

For example, the following defines a function called button_clicked():

def button_clicked():
    print('Button clicked')
Code language: Python (python)

After that, you can associate the function with the command option of a button widget:

ttk.Button(root, text='Click Me',command=button_clicked)
Code language: Python (python)

Note that you pass the callback without parentheses () within the command option. Otherwise, the callback would be called as soon as the program runs.
"""


# The following is the full program that illustrates how to assiciate the button_clicked callback function with the button widget:

import tkinter as tk 
from tkinter import ttk 


root = tk.Tk()

def button_clicked():
	print("Button Clicked")

button = ttk.Button(root, text="Click Me", command = button_clicked)
button.pack()


root.mainloop()


# Tkinter Button Command Arguments:

# if we want to pass arguments to a callback function
# we can use a lambda expression.

# First Define a function that accepts arguments:
"""

def callback_function(args):
	# do something 

Then define a lambda expression and assign it to the command option.
Inside the lambda expression, invoke the callback function:

ttk.Button(
root, 
text="Button",
command = lambda: callback_function(args))

"""

# The following program illustrates how to pass an arguments to the callback function assiciated with the button command:


import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()

def select(option):
	print(option)

ttk.Button(root, text="Rock", command=lambda: select('Rock')).pack()
ttk.Button(root, text="Paper", command=lambda: select('Paper')).pack()
ttk.Button(root, text="Scissors", command=lambda: select('Scissors')).pack()

root.mainloop()



"""
Limitations of command binding

First, the command option isn’t available in all widgets. It’s limited to the Button and some other widgets.

Second, the command button binds to the left-click and the backspace. It doesn’t bind to the Return key.

To check this you can move focus to a button in the program above and press the backspace and return keys. This is not really user-friendly. Unfortunately, you cannot change the binding of the command function easily.

To overcome these limitations, Tkinter provides an alternative way for associating a function with an event, which is called event binding.
Summary

    Assign a function name to the command option of a widget is called command binding in Tkinter.
    The assigned function will be invoked automatically when the corresponding event occurs on the widget.
    Only few widgets support the command option.
"""


















