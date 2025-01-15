# Tkinter Frame

# A frame is a widget that display as a simple rectangle.
# Typically we use a frame to organize other widgets both visually and at the coding level .

# To create a frame, we use the ttk.Frame class
# frame = ttk.Frame(container, **options)

# A frame has various configuration object which determine its appearance.

# Frame Size:
# The size of a frame is deternimed by the size and layout of the widget it contains.

# We can explicitly specify the height and width of the frame when we create it.

# frame = ttk.Frame(container, height, width)

# Paddings
# The padding allows us to add extra space arround the inside of the frame
# Paddings are in pixels. and we can specify padding for each side of the frame separately lile

# frame['padding'] = (left, top, right, bottom)

# Example:
# frame['padding'] = (5, 10, 5, 10)

# Or we can specify paddings for left, right and top, bottom
# frame['padding'] = (5, 10)
# Here the left and right padding are 5 and the op and bottom paddings are 10.
# If the paddings are all sides are the same, we can specify the padding like
# frame['padding'] = 5

## Frame Border
#By default, the border width of a frame is zero. In other words, the frame has no border.

#To set a border for a frame, you need to set both border with and border style.

#The border width of a frame is in pixels. The border style of a frame can be flat, groove, raised, ridge, solid, sunken. The default border style of a frame is flat.

#The following example sets the border width of the frame to 5 pixels and border style of the frame to sunken.

#frame['borderwidth'] = 5
#frame['relief'] = 'sunken'

# The following program illustrates how to create the Replace window above:

import tkinter as tk
from tkinter import ttk


def create_input_frame(container):

    frame = ttk.Frame(container)

    # grid layout for the input frame
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)

    # Find what
    ttk.Label(frame, text='Find what:').grid(column=0, row=0, sticky=tk.W)
    keyword = ttk.Entry(frame, width=30)
    keyword.focus()
    keyword.grid(column=1, row=0, sticky=tk.W)

    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Warp Around Checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text="Warp around",
        command=lambda: print(wrap_around.get())
    )
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)


    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame


def create_button_frame(container):
    frame = ttk.Frame(container)

    frame.columnconfigure(0, weight=1)

    ttk.Button(frame, text="Find Next").grid(column=0, row=0)
    ttk.Button(frame, text="Replace").grid(column=0, row=1)
    ttk.Button(frame, text="Replace All").grid(column=0, row=2)
    ttk.Button(frame, text="Cancel").grid(column=0, row=3)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame

def create_main_window():

    # root window
    root = tk.Tk()
    root.title("Replace")
    root.geometry('400x150')
    root.resizable(0, 0)
    # windows only (remove the minimum/maximum button)
    root.attributes('-toolwindow', True)


    # layout on the root window
    root.columnconfigure(0, weight=4)
    root.columnconfigure(1, weight=1)

    input_frame = create_input_frame(root)
    input_frame.grid(column=0, row=0)

    button_frame = create_button_frame(root)
    button_frame.grid(column=1, row=0)

    root.mainloop()

if __name__ =="__main__":
    create_main_window()
