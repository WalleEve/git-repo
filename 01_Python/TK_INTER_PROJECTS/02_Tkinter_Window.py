# Let's start with a simple program that consists of a window.

import tkinter as tk

root = tk.Tk()

root.mainloop()

# The root window has a title that defaults to tk. It also has three system buttons including Minimize, maximize and Close

# Changing the window title

# To change the window's title we use the title() method

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window Demo")

root.mainloop()

# To get the current title of the window, we use  the title() method with no argument

import tkinter as tk

root = tk.Tk()
root.title("Main Window")
cTitle = root.title()
print(cTitle)

root.mainloop()



# CHANGING WINDOW SIZE AND LOCATION

# In Tkinter, the position and size of a window on the screen is determined by geometry.
"""
_______________________________________> xrange
|
|       +y
|       _________________
|   +x  |               |
|       |               | height
|       |               |
|       |               |
|       _________________
|           width
yrange

window.geometry("widthxheight+-x+-y")

In this specification:

    The width is the window’s width in pixels.
    The height is the window’s height in pixels.
    The x is the window’s horizontal position. For example, +50 means the left edge of the window should be 50 pixels from the left edge of the screen. And -50 means the right edge of the window should be 50 pixels from the right edge of the screen.
    The y is the window’s vertical position. For example, +50 means the top edge of the window should be 50 pixels below the top of the screen. And -50 means the bottom edge of the window should be 50 pixels above the bottom of the screen.

"""

# To change the size and position of a window, we use the geometry() method.

# window.geometry(new_geometry)

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Window")
root.geometry("600x400+50+100")

root.mainloop()


# Sometimes we want to center the window on the screen.

import tkinter as tk

root = tk.Tk()
root.title('Tkinter Window - Center')
window_width = 300
window_height = 200

# get the sceen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(f"screen_width: {screen_width}, screen_height: {screen_height}")

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
print(f"center_x: {center_x}, center_y: {center_y}")

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

root.mainloop()

"""
How it works.

    First, get the screen width and height using the winfo_screenwidth() and winfo_screenheight() methods.
    Second, calculate the center coordinate based on the screen and window width and height.
    Finally, set the geometry for the root window using the geometry() method.

"""
# If we want to get the current geometry of a window, we can use the geometry() method without providing any argument.

# window.geometry()

import tkinter as tk

root = tk.Tk()
current_geometry = root.geometry()
print(f"current_geometry:{current_geometry}")

# set new geometry
root.geometry("600x400+50+50")
current_geometry = root.geometry()
print(f"new_current_geometry:{current_geometry}")


root.mainloop()

# Note: Here we can get the only geometry of the screen not the height and width of the window.


# RESIZING BEHAVIOR:

# By default we can resize the width and height of a window.
# To prevent the window from resizing we can use the resizable() method.

# window.resizable(width.height)

# The resizable() method has two parameters that specify wheather the width and height of the window can be resizable.
import tkinter as tk

root = tk.Tk()
root.geometry("600x400+50+50")
root.resizable(False, False)


root.mainloop()


# When a window is resizable, we can specify the minimum and maximum sizes using the minsize() and maxsize() methods:

# window.minsize(min_width, min_height)
# window.maxsize(max_width, max_height)

import tkinter as tk

root = tk.Tk()
root.geometry("600x400+50+50")
#root.resizable(False, False)
root.minsize(100, 100)
root.maxsize(600, 400)

root.mainloop()


# TRANSPARENCY:

# Tkinter allows us to specify the transparency of a window by setting its alpha cannel ranging from 0.0 (fully transparent) to 1.0 (fully opaque)

# window.attributes("-alpha", 0.5)

import tkinter as tk

root = tk.Tk()
root.geometry("600x400+50+50")
root.title("Tkinter Window")
root.geometry("600x400+50+50")
root.resizable(False, False)
root.attributes('-alpha', 0.5)

root.mainloop()



# WINDOW STACKING ORDER

# The window stack order refers to the order of window placed on the screen from bottom to top.
# The closer window is on top of the stack and it overlaps the one lower.
# To ensure that a window is always at the top of the stacking order, we can use the -topmost attribute

# window.attributes('-topmost', 1)

# to move a window up or down of the stack, we can use the lift() and lower() methods:

# window.lift()
# window.lift(another_window)

# window.lower()
# window.lower(another_window)

import tkinter as tk

root = tk.Tk()
root.geometry("600x400+50+50")
root.title("Tkinter Window")
root.geometry("600x400+50+50")
root.resizable(0, 0)
root.attributes('-topmost', 1)

root.mainloop()

# CHANGING THE DEFAULT ICON:
"""
Tkinter window displays a default icon. To change this default icon, you follow these steps:

    Prepare an image in the .ico format. If you have the image in other formats like png or jpg, you can convert it to the .ico format. There are many online tools that allow you to do it quite easily.
    Place the icon in a folder that can be accessible from the program.
    Call the iconbitmap() method of the window object.
"""
# The following program illustrates how to change the default icon to a new one:

import tkinter as tk

root = tk.Tk()
root.geometry("600x400+50+50")
root.title("Tkinter Window")
root.geometry("600x400+50+50")
root.resizable(False, False)
root.iconbitmap("C:\\Users\\Mahfuze\\Documents\\GitHub\\Python3\\Tkinter_Tutorial\\images\\pythontutorial-1-150x150.ico")

root.mainloop()

"""

Summary

    Use the title() method to change the title of the window.
    Use the geometry() method to change the size and location of the window.
    Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
    Use the window.attributes('-alpha',0.5) to set the transparency for the window.
    Use the window.attributes('-topmost', 1) to make the window always on top.
    Use lift() and lower() methods to move the window up and down of the window stacking order.
    Use the iconbitmap() method to change the default icon of the window.

"""
