# Tkinter  # PYQT5 # KIVY # 

# Python inbuild module 
# which help us to create desktop level application 

import tkinter as t 

root = t.Tk()
root.geometry('400x400')
root.title('My Application')
root.resizable(False, False)

t.Label(root, text="MY Application", font=('Times New Roman', 15)).pack()






root.mainloop()




