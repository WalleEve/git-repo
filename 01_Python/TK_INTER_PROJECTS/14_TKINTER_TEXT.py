# Tkinter Text
# The Text widget allows us to display and edit -line textarea with various styles.
# Beside the plain text, the Text widget supports embedded image and links.

# To create a text widget, we use the following syntax:

# text = tk.Text(master, conf={}, **kw)

# The master is the parent component of the Text widget
# The cnf is a dictionary that specifies the widget's configuration.
# The kw is one or more keyword arguments used to configure the Text widget.

# Note that the Text widget is only available in the Tkinter module, not in the Tkinter.ttk module.

# The following example created s Text widget with eight row and placed it on the roor window.

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

root.mainloop()

# In this example, the height argument specifies the number of rows of the Text widget.

# Inserting Initial content:

# To insert into the text area, we use the insert() method

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack()

text.insert('1.0', "This is a Text widget demo")

root.mainloop()


# The first argument of the insert() method is the position where we want to insert the text.

# The position has the following format:
# 'line.column'

# In the above example, '1.0' means line 1, character 0, which is the first character of the first line on the text area.

## Retriving the text value:
# To retrive the contents of a Text widget, we use its get() method

# text_content = text.get('1.0', 'end')

# The get() method accepts two arguments, The first argument is the start position, and the second is the end position.

# To retrive only part of the text, we can specify different start and end positions.

## Disabling the Text widget

# To prevent users from changing the contents of a Text widget, we can disable it by setting the state opton to 'disabled'

# text['state'] = 'disabled'

# To re-enable editing, we can change the state option back to normal.

# text['state'] = 'normal'
