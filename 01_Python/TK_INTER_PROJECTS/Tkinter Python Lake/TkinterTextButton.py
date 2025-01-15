# tkinter.Button(command=create text)
# The code create the text() through button and then destry and create new button compose.

from tkinter import *
from tkinter import Text
import tkinter

master = tkinter.Tk()



def message():
    compose_button.destroy()

    send_message_button = tkinter.Button(master, text="Submit Message")
    send_message_button.pack()

    compose_text=tkinter.Text(master)
    compose_text.pack()
    


compose_button=tkinter.Button(master, text="Compose Message", command=message)
compose_button.pack()

master.mainloop()
