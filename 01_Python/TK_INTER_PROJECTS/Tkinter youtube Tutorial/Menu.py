# Menu Button
from tkinter import *

root = Tk()
root.geometry("300x200")

# Function to call from submenu
def random():
    print("This is test Text")
print("This is test Text")


# Main Menu Line Config
mainMenu = Menu(root)
root.configure(menu = mainMenu)
subMenu = Menu(mainMenu)
# Adding main menu:
mainMenu.add_cascade(label="File", menu=subMenu)

# Adding Sub Menu:
subMenu.add_command(label = "New FIle", command=random)
subMenu.add_command(label = "Open File", command=random)

# add Separator:
subMenu.add_separator()
subMenu.add_command(label = "Print", command=random)

root.mainloop()
