# Class 2- IMAGE, Pillow :
"""
Image of different formats can be created through the corresponding subclass of tkinter.Image
. BitmapImage for image in XBM format
. PhotoImage for images in PGM, PPM, GIF and PNG formats.

The image object can then be used whenever an image option is supported by
some widget (e.g. labels, buttons, menus)

The pillow package add support for format such as BMP, JPEG, TIFF and WebP


"""
from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.geometry("1200x400")
# Label :
LabelName = Label(text="AngryBird")

# photo = PhotoImage(file="red.png")

image = Image.open("maxresdefault.jpg")
photo = ImageTk.PhotoImage(image)
LabelPhoto = Label(image=photo).pack()
LabelName.pack()

root.mainloop()
