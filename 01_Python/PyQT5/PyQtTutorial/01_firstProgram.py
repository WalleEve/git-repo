# Creating the first PyQt Program 

from PyQt5.QtWidgets import QApplication, QWidget

# create the QApplication
app = QApplication([])

# create the main window
window = QWidget(windowTitle = "Hello World")
window.show()


# Start the event loop
app.exec()

