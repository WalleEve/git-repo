# 6. Using QStackedLayout (Stacked Layout)
# The QStackedLayout allows you to stack widgets on top of each other. Only one widget is visible at a time, similar to tabbed interfaces.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackedLayout Example')

        # Create a stacked layout
        layout = QStackedLayout()

        # Create widgets to be stacked
        widget1 = QLabel('This is Widget 1')
        widget2 = QLabel('This is Widget 2')

        # Add widgets to the stacked layout
        layout.addWidget(widget1)
        layout.addWidget(widget2)

        # Show the second widget (index 1)
        layout.setCurrentIndex(1)

        # Set the layout for the window
        self.setLayout(layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
