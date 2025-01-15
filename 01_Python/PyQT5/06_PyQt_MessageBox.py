# Dislogs and Message Boxes 
# Dialogs and message boxes are common in applications for giving feedback or asking for input.

import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QMessageBox 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Message Box Example")
		
		self.button = QPushButton("show Message", self)
		self.button.clicked.connect(self.show_message)
		
		
	def show_message(self):
		msg_box = QMessageBox()
		msg_box.setText("This is a message box.")
		msg_box.exec_()  # show the message box 
		
		
		
if __name__ == "__main__":
	application = QApplication(sys.argv)
	app = MainWindow()
	app.show() 
	sys.exit(application.exec_())


# Key Concepts 
# QMessageBox: A dialog box that display a message 
# exec_(): Executes the dialog and waits for a response.

