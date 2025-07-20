# Below is an example of a PyQt5 application that uses a QGridLayout, QTabWidget, 
# and a QTextEdit (for a large multiline text box) to create a simple user interface 
# with tabs and a grid layout, including a large text box for entering a multiline address.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTabWidget, QPushButton, QLabel, QTextEdit, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Full Example')
        self.setGeometry(100, 100, 600, 400)

        # Create main layout
        main_layout = QVBoxLayout()

        # Create QTabWidget (Tabs)
        tab_widget = QTabWidget()

        # Tab 1: Simple Grid Layout with labels and buttons
        tab1 = QWidget()
        grid_layout = QGridLayout()

        grid_layout.addWidget(QLabel('Name:'), 0, 0)
        grid_layout.addWidget(QLabel('John Doe'), 0, 1)

        grid_layout.addWidget(QLabel('Phone:'), 1, 0)
        grid_layout.addWidget(QLabel('+1 234 567 890'), 1, 1)

        grid_layout.addWidget(QLabel('Email:'), 2, 0)
        grid_layout.addWidget(QLabel('john.doe@example.com'), 2, 1)

        grid_layout.addWidget(QPushButton('Submit'), 3, 0, 1, 2)

        tab1.setLayout(grid_layout)

        # Tab 2: A large QTextEdit for multiline address input
        tab2 = QWidget()
        vbox_layout = QVBoxLayout()

        address_label = QLabel('Enter Address:')
        vbox_layout.addWidget(address_label)

        address_textbox = QTextEdit()
        address_textbox.setPlaceholderText("Write your address here...")
        vbox_layout.addWidget(address_textbox)

        tab2.setLayout(vbox_layout)

        # Add tabs to the QTabWidget
        tab_widget.addTab(tab1, "Grid Layout")
        tab_widget.addTab(tab2, "Address Input")

        # Add the tab widget to the main layout
        main_layout.addWidget(tab_widget)

        # Set the main layout for the window
        self.setLayout(main_layout)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
