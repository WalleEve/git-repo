# # Tkinter Progressbar widget
# A Progressbar widget allows us to give fedback to the user about the progress of a long-running task.
# To create a Progressbar widget, we use the ttk.Progressbar class.

# ttk.Progressbasr(container, **options)

# The following shows the typical parameter to create a Progressbar widget.

# ttk.Progressbar(container, orient, length, mode)

#. The container is the parent component of the progressbar.
#. The orient can be either 'horizontal' or 'vertical'
#. The length represent the width of horizontal progress bar or the height of a vetical progressbar.
#. The mode cann be either 'determinate' or 'indeterminate'

# The indeterminate mode:
# In the indeterminate mode the progressbar shows an indicator that bounces back and forth between the ends of the widget.
# Typically, we use the indetermiate mode when we don't know how to acurately measure the time that the long-running task to complete.

# The determinate mode:
# In the determinate mode, the progressbar shows an indicator from the biginning to the end of the widget.

# if we know how to measure the relative progress, we can use the determinate mode.

# The import methods of a progressbar:
# The progressbar has the following import methods:
#. start([interval]) - start moving the indicator every interval milliseconds. The intercal default to 50ms
#. step([delta]) - increase the indicator value by delta. The delta default to 1 millisecond.
#. stop() - stop moving the indicator of the progressbar.

# Tkinter Progressbar Example;
# Tkinter Progressbar in the indeterminate mode example:
# The following program illustrate how to create a progressbar in the indetermiate mode. Of we click start button, the progressbar starts moving the indicator. When we click the stop button, the progressbar stop moving the progress indicator

import tkinter as tk
from tkinter import ttk

# root widow
root = tk.Tk()
root.geometry("300x120")
root.title("Progressbar Demo")

root.grid()

#progressbar
pb = ttk.Progressbar(
root,
orient = "horizontal",
mode="indeterminate",
length=280
)

pb.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# start button
start_button = ttk.Button(
root,
text="Start",
command = pb.start
)

start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
root,
text='Stop',
command=pb.stop
)

stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W )

root.mainloop()
