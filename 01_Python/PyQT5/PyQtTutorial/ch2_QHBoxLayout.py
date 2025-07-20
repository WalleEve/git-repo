# 2. Using QHBoxLayout (Horizontal Layout)
# This layout arranges widgets horizontally (left to right).

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QHBoxLayout Example')

        # Create a horizontal layout
        layout = QHBoxLayout()

        # Add buttons to the layout
        layout.addWidget(QPushButton('Button 1'))
        layout.addWidget(QPushButton('Button 2'))
        layout.addWidget(QPushButton('Button 3'))

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
