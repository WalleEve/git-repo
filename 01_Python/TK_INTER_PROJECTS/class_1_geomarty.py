from tkinter import *

root = Tk()
# Geomarty (height x width)
root.geometry("400x300")

# Max Size for GUI (width, height)
root.maxsize(600, 600)

# Min Size for GUI (width, height)
root.minsize(100, 200)


# Label to dispay any text in GUI
labName = Label(text="Name:")
labName.pack() # Pack is used to dispay the value on GUI


root.mainloop()
