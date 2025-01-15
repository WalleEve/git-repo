# Creating Menues and Toolbars 

import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtWidgets import QMenuBar

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Menu Bar Example")
		
		# Create a menu bar 
		menu_bar = self.menuBar()
		
		# Add a file menu 
		file_menu = menu_bar.addMenu("File")
		
		# Add actions (menu itmes)
		open_action = file_menu.addAction("Open")
		exit_action = file_menu.addAction("Exit")
		
		
		# Connect the exit action 
		exit_action.triggered.connect(self.close) # close the window 


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())