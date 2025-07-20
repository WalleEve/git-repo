# 1. QGridLayout (Grid Layout)
# QGridLayout arranges widgets in a grid with rows and columns.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QGridLayout Example')

        # Create a grid layout
        layout = QGridLayout()

        # Add widgets to the grid layout
        layout.addWidget(QLabel('Name:'), 0, 0)
        layout.addWidget(QLabel('John Doe'), 0, 1)

        layout.addWidget(QLabel('Phone:'), 1, 0)
        layout.addWidget(QLabel('+1 234 567 890'), 1, 1)

        layout.addWidget(QLabel('Email:'), 2, 0)
        layout.addWidget(QLabel('john.doe@example.com'), 2, 1)

        layout.addWidget(QPushButton('Submit'), 3, 0, 1, 2)  # Spanning 2 columns

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
