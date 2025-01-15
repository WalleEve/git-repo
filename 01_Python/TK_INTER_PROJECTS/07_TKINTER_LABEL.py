# Tkinter Label:
# Tkinter Label widget is used to diaply a text or image on the screen. To use a Label widget, we use the following syntax:

# label = ttk.Label(container, **options)

# The Label widget has many options that allow to customize its appearance:

# anchor : When the text and/or image are smaller than the width, the anchor option determines where to position them tk.W, tk.CENTER or tk.E or left, center, and right alignment respectively.

# backgroung : Set the backgroung color for the label

# borderwidth : Add a border around the label 

# class_ : Specify a custom widget class name for changing the label's appearance.

# compound : Specify how to display both text and image on the Label.

# cursor : Specify the mouse cursor's appearance when the mouse is over the widget.

# font : Specify the font style for displaying text.

# foreground : Specify the color of the text 

# image : Specify an image or image to show in addition to text or instead of text.

# justify : If the text contains newline character, the justify option specify how each line is positioned horizontally. The valid value are tk.LEFT (left-justify), tk.CENTER(center) and tk.RIGHT(right-justify)

# padding : Add more space arroung the label.

# relief : Use this option to create an effect for the Label .e.g, flat, raised, sunken, groove, and ridge.

# takefocus : is a boolean value that specify wheather the label is visited during focus traversal, It defaults to False which show doesn't get focus.

# text : Specify a string of text to show in the widget

# textvariable : A StringVar instance that holds the text value of the widget. It overrides the text option if both textvariable and text are available.

# underline : Specify the position of the letter that shuld be underlined e.g, underline  = 0 would be the letter E in the text='Exit'

# width : Specify the number of characters to show 

# wraplength : Chop the text into the lines which less than the length specified by the wraplngth option.


# Display a regular label 

# the following program shows how to display a regular label on the root window.

import tkinter as tk 
from tkinter import ttk 

root = tk.Tk() 
root.geometry('300x200')
root.resizable(False, False)
root.title("Label Widget Demo")
root.iconbitmap("C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\pythontutorial-1-150x150.ico")

# show a lable 
label = ttk.Label(root, text="This is a lable")
label.pack(ipadx=10, ipady=10)


root.mainloop()


# Setting a specific font for the Label.

# To setup a particular font for a label, we pass the font keyword argument to the Label constructor 

# font = ('font name', font_size)

# The font keyword argument is a tuple that contains font name and size
# font('Helvetica', 14)


import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Label Widget Demo")


# Label with a specific font
label = ttk.Label(
	root,
	text="A Label with the Helvetica font",
	font=("Helvetica", 14)
	)
label.pack(ipadx=10, ipady=10)

root.mainloop()


# Displaying an image 

# To use a Label widget to display an image
# First creae a PhotoImage widget by passing the path to the photo to the PhotoImage constructor.

# photo = tk.PhotoImage(file="./aeesta/python.png")

# Second, assign the PhotoImage object to the image option of the Label widget.

# Label(..., image=photo)

import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Label Widget Image")

# Display an image label
photo = tk.PhotoImage(file="C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\pylogo.png")
imagel_label = ttk.Label(
	root,
	image=photo,
	padding=5 
	)
imagel_label.pack() 

root.mainloop()


"""
To display both text and image, you’ll use the text attribute and compound option.

The compound option specifies the position of the image relative to the text. Its valid values are:
Compound	Effect
'top'	Display the image above the text.
'bottom'	Display the image below the text.
'left'	Display the image to the left of the text.
'right'	Display the image to the right of the text.
'none'	Display the image if there’s one, otherwise display the text. The compound option defaults to 'none'.
'text'	Display the text, not the image
'image'	Display the image, not the text.
"""

# The following program shows how to display both text and image on a label.

import tkinter as tk 
from tkinter import ttk  


root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Label Widget Image")

# Display an image label 
photo = tk.PhotoImage(file="C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\pylogo.png")

image_label = ttk.Label(
	root,
	image=photo,
	text="Python",
	compound="top")

image_label.pack()

root.mainloop()


# OR We can use PIL module.

import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk  


root = tk.Tk()
root.geometry("300x300")
root.resizable(False, False)
root.title("Label Widget Image")

# Read the Image:
image = Image.open("C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\pythonim2.jpg")

# Resize the image:
image = image.resize((150, 100))
# Display an image label 
photo = ImageTk.PhotoImage(image)

image_label = ttk.Label(
	root,
	image=photo,
	text="Python",
	compound="top")

image_label.pack()

root.mainloop()
































