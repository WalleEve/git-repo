# Import QApplication and all the required widgets from PyQt6.QtWidgets.
# Create an instance of QApplication.
# Create your application’s GUI.
# Show your application’s GUI.
# Run your application’s event loop, or main loop.


# PyQt Signals and Slots 


from PyQt5.Widgets import QWidget
from PyQt5.Widgets import QApplication, QMainWindow

import sys


class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()

		self.setWindowTitle("My App")




if __name__ == "__main__":

	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exec_()




