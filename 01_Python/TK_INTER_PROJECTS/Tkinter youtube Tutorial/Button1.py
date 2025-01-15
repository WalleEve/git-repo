# Button inside the frame .
from tkinter import *

root = Tk()
root.title("Button")
# root.geometry(width=200, hight=200)

topFrame = Frame(root)
topFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Botton1", bg="Blue")
button1.pack(side=LEFT)
button2 = Button(topFrame, text="Botton2", bg="Red")
button2.pack(side=LEFT)

button3 = Button(bottomFrame, text="Botton3", bg="Pink")
button3.pack(side=LEFT)
button4 = Button(bottomFrame, text="Botton4", bg="Yellow")
button4.pack(side=LEFT)

root.mainloop()
