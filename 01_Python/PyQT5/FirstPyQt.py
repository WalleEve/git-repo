# Create our First PyQt5 Window:

# Basic structure of a PyQt5 application 

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow

# Create main window 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("My First PyQt5 WIndow")
		self.setGeometry(100, 100, 700, 400) # x, y, width, height
		
	
if __name__ == "__main__":
	app = QApplication(sys.argv) # create the application 
	window = MainWindow() # Create instance of main window 
	window.show() # Display the window 
	sys.exit(app.exec_()) # Execute the app 