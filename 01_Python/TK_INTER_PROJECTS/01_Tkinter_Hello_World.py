# CREATE A WINDOW:

# The following program shows how to display a window on the screen.

import tkinter as tk

root = tk.Tk()

root.mainloop()

# First import the tkinter module as tk to the program.
# Second, create as instace of the tk.Tk class that will create the application window.
# By convention, the main window in tkinter is called root. But we can use any other name
# Ex: main = tk.Tk()

# Third, call the mainloop() method of the main window object. The mainloop() keeps the window visible on the screen. if we do not call the mainopp() method the window will display and disappear immediately. Also the mainloop() method keeps the window displaying and running until we close it.

# Displaying a Lable

# Now we can place a component on the window. In Tkinter, components are called widgets.

# The following adds a label widget to the root window

import tkinter as tk

root = tk.Tk()

# place a label on the root Window
message = tk.Lable(root, text="Hello, World")
message.pack()

# keeps the window displaying
root.mainloop()

# To create a widget that belongs to a container, we use the following syntax

# widget = WidgetName(container, **options)

# The container is the parent window or frame that we want to place the widget
# The options is one or more keyword arguments that specify the configurations'of the widget.
# the meggage.pack() statement positions the Label on the window.
