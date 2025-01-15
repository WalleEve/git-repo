from tkinter import *
screen = Tk()
screen.geometry('300x300')
label1 = Label(screen, text="""This is Original Window""")
label1.pack()
#you can make as many Toplevels as you like
new_window = Toplevel(screen)
new_window.geometry('300x300')
label2 = Label(new_window, text="""This is Toplevel Window""")
label2.pack()
screen.mainloop()
