# Button(command = webbrowser.open_new())
# The URL is opened through tkinter.Button() through its command option.

import webbrowser
from tkinter import *

def url():
    url = webbrowser.open_new("www.pythonlake.com")

master = Tk()
master.geometry("100x200")

button = Button(master, text = "Pythonlake.com", command=url)
button.pack()

master.mainloop()
