## Tkinter ScrolledText Widget
#We’ve learned how to create a Text widget and how to link a vertical Scrollbar to the text widget.

#To make it more convenient, Tkinter provides you with the ScrolledText widget which does the same things as a text widget linked to a vertical scroll bar.

#To use the ScrolledText widget, you need to import the ScrolledText class from the tkinter.scrolledtext module.

#Technically, the ScrolledText class inherits from the Text class.

#The ScrolledText widget uses a Frame widget inserted between the container and the Text widget to hold the Scrollbar widget.

#Therefore, the ScrolledText has the same properties and methods as the Text widget. In addition, the geometry manager methods including pack, grid, and place are restricted to the Frame.

# Tkinter ScrolledText Widget example
# The following program illustrates how to create a ScrolledText widget:

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title("ScrolledText Widget")

st = ScrolledText(root, width=50, height=10)
st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()
# First import the tkinter module and the ScroledText call from the tkinter.scrolledtext
# second create the root window and set its title to "ScrolledText Widget"
# Third, create a new ScrolledText widget and display it on the root window.
# Finaly, start the mainloop.

# Here we can write the same using object-oriented programming approach

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class App(tk.Tk):
    def __init__(self):
        self.title("ScrolledText Widget")
        st = ScrolledText(self, width=50, height=10)
        st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
"""
Summary

    Use the Tkinter ScrolledText widget to create a Text widget with a vertical Scrollbar.
"""
