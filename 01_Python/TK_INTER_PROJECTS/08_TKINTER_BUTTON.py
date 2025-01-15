# TKINTER BUTTON:

"""
Button widgets represent a clickable item in the applications.
Typically we use a text or an image to display the action that will bebe perform when clicked.

Buttons can display text in a single font. However the text can span 
miltiple lines.
On top of that we can make one of the character underline to make a keyboard shortcut.

To invoke a function or a method of a class automatically when the button  is clicked, 
we assign its command option to the function or method.
This is called the command binding in Tkinter.


To create a button, we use the ttk.Button constructor 

button = ttk.Button(container, **options)

A Button has many options. However the typical ones are ike:

button = ttk.Button(container, text, command)

# The container is the parent component on which we place the button.
# The text is the lable of the button 
# The command specifies a callback function that will be called automatically when the button clicked.

"""

# Command callback:

# The command option associate the buttos's action with a function or method of a class.
# When we click or press the button, it'll automatically invoke a callback function.

# To assign a callback to the command option, we can use a lambda expression:
"""
def callback():
	pass 

ttk.Button(
	root, 
	text="Demo Button",
	command = callback)


# If the function contains one expression, we use a lambda expression:

ttk.Button(
root, 
text = "Demo Button",
command = lambda_expression)


"""

# Button State:

"""
The default state of a button is normal. In the normal state, the button will respond to 
the mouse event and keyboard press by invoking the callback function assigned to its 
command option.

The button can also have the disable state, In the disable state, a button is greyed out and doesn't
respond to the mouse event and kayboard presses.

To control the state of a button, we use the state() method.

# set the disabled flag
button.state(['disable'])


# remove the disabled flag
button.state(['!disabled'])

"""

# TKINTER Button Example:

#1: Simple Tkinter button example.
# The following program show to display an Exit button. When we click it, the program is retminated.

import tkinter as tk 
from tkinter import ttk  


# root window 
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Button Demo")


# exit button 
exit_button = ttk.Button(
	root,
	text="Exit",
	command = lambda: root.quit())

exit_button.pack(
	ipadx=5,
	ipady=5,
	expand=True)

root.mainloop()

# The command of the button is assigned to a lambda expression that closes the root window.


# Tkinter image button :

# The gollowing program shows how to display an image button.

import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo 


# root Window:
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Image Button Demo")


# download button 
def download_clicked():
	showinfo(
		title="Information",
		message="Download button clicked")


download_icon = tk.PhotoImage(file="C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\dwnl.png")
download_button = ttk.Button(
	root, 
	image=download_icon,
	command=download_clicked)

download_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()


import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showinfo 


# root Window:
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Image Button Demo")


# download button 
def download_clicked():
	showinfo(
		title="Information",
		message="Download button clicked")


download_icon = tk.PhotoImage(file="C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\dwnl.png")
download_button = ttk.Button(
	root, 
	image=download_icon,
	command=download_clicked)

download_button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()


# Display an image button 

# To display both text and image on a buton, we need to use the compound option. if we don't, the button will display the text only, not the image.

# The following shows how to display both text and image on a button.
import tkinter as tk 
from tkinter import ttk  
from tkinter.messagebox import showinfo 


# root window:

root = tk.Tk() 
root.geometry("400x200")
root.resizable(False, False)
root.title("Image Button Demo")


# download button handler 
def download_clicked():
	showinfo(
		title="Information",
		message="Download button clicked!"
	)


download_icon = tk.PhotoImage(file="C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\dwnl.png")

download_button = ttk.Button(
	root,
	image = download_icon,
	text="Download",
	compound=tk.LEFT,
	command = download_clicked
)

download_button.pack(
	ipadx=5,
	ipady=5,
	expand=True
)

root.mainloop()







"""
Summary

    Use the ttk.Button() class to create a button.
    Assign a lambda expression or a function to the command option to respond to the button click event.
    Assign the tk.PhotoImage() to the image property to display an image on the button.
    Use the compound option if you want to display both text and image on a button.

"""








