# Advanced Widget 

# We can create tabels to show data. 

import sys 

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QLabel, QPushButton 
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QLineEdit 
from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Table Widget Example")
		
		table = QTableWidget(3, 2, self) # Create a table with 3 rows and 2 columns 
		
		table.setItem(0, 0, QTableWidgetItem("Row0, Col 0"))
		table.setItem(0, 1, QTableWidgetItem("Row 0, Col 1"))
		


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

# Key Concepts 
# QTableWidget: Display data in a table.
# setItem(row, col, QTableWidgetItem): Sets an itme in the table 

