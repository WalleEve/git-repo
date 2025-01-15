import tkinter

master = tkinter.Tk()
master.title("Button")

button1 = tkinter.Button(master, text="B1", bg="Red").grid(row=0, column=0)
button2 = tkinter.Button(master, text="B2", bg="Blue").grid(row=0, column=1)
button3 = tkinter.Button(master, text="B3").grid(row=0, column=2)
button4 = tkinter.Button(master, text="B4", bg="Orange").grid(row=0, column=3)
button5 = tkinter.Button(master, text="B5", bg="Pink").grid(row=0, column=4)

master.mainloop()
