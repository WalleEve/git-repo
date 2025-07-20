# 3. Using QGridLayout (Grid Layout)
# A grid layout arranges widgets in a matrix-like structure (rows and columns).


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QGridLayout Example')

        # Create a grid layout
        layout = QGridLayout()

        # Add widgets to the grid layout
        layout.addWidget(QPushButton('Button 1'), 0, 0)  # Row 0, Column 0
        layout.addWidget(QPushButton('Button 2'), 0, 1)  # Row 0, Column 1
        layout.addWidget(QPushButton('Button 3'), 1, 0)  # Row 1, Column 0
        layout.addWidget(QPushButton('Button 4'), 1, 1)  # Row 1, Column 1

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
