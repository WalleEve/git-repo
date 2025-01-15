# Tkinter slider widget

# A slider allows us to enter a value by moving an indicator.
# A slider can be vertical or horizontal

# To create a slider, we'll use the ttk.Scale() contructor
# ttk.Scale(contaier, from_, to)

# The container specifies the parent component of the slider
# The from_ and to option specify the minimum and maximum values of the slider.
# Since from is a keyword in Python, Tkinter used from_ instead.

# By default a slider is horizontal. To specify how the slider is arragnes, we use the orient option which can be horizontal or vertical
"""
slider = ttk.Scale(root, from_=0, to=100, orient="vertical", #horizontal
)
"""

## Getting current value
# To get the current value of the slider, we can assign a DoubleVar to the variable of the silder like
"""
current_value = tk.DoubleVar()
slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', variable=current_value)
"""

# Another way to get the current value of slider is to call the get() method of the slider

# slider.get()

## Executing a callback
# To run a function whenever the value of the slider changes, we can assign it to the command option as follows
"""
def slider_change(event):
    print(slider.get())

slider = ttk.Scale(root, from_=0, to=100, orient="horizontal", variable=current_value, command=slider_changed)
"""

# Notice that calling a function when the value of the slider changes can cause performance problems.

## Disabling the slider:

# To disable the slider, we set itss state to 'disabled'.
# To re-enable it, we set its state to 'normal'

# slider['state'] = 'disable'
# slider['state'] = 'normal'

# By default, the slider's state is normal.

# Tkinter slider example;
# The following program illustrate how to use a Tkinter slider widget. The label will update the current value of the slider when we change the slider's value.

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(False, False)
root.title("Slider Demo")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# slider current value
current_value = tk.DoubleVar()

def get_current_value():
    return "{: .2f}".format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

# label of the slider
slider_label = ttk.Label(root, text="Slider:")
slider_label.grid(column=0, row=0, sticky='w')

# slider
slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)

slider.grid(column=1, row=0, sticky='we')

# current_value label
current_value_label  =ttk.Label(root, text="Current Value: ")
current_value_label.grid(row=1, columnspan=2, sticky='n', ipadx=10, ipady=10)

# value label
value_label = ttk.Label(root, text=get_current_value())
value_label.grid(row=2, columnspan=2, sticky='n')

root.mainloop()


"""
Summary

    Use the ttk.Scale() to create a slider widget.
    Use the scale.get() or the variable option to get the current value of the slider.
    Use the command option to assign a function that will execute when the slider’s value changes.

"""
