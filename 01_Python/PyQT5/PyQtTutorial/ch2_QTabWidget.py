# 2. QTabWidget (Tabs)
# QTabWidget allows you to create a tabbed interface.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTabWidget Example')

        # Create the tab widget
        tab_widget = QTabWidget()

        # Tab 1: Simple label
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()  # Create a layout for Tab 1
        tab1_layout.addWidget(QLabel('This is Tab 1'))  # Add label to the layout
        tab1.setLayout(tab1_layout)  # Set the layout for Tab 1

        # Tab 2: Another label
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()  # Create a layout for Tab 2
        tab2_layout.addWidget(QLabel('This is Tab 2'))  # Add label to the layout
        tab2.setLayout(tab2_layout)  # Set the layout for Tab 2

        # Add tabs to the widget
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        # Set the layout for the window
        main_layout = QVBoxLayout()  # Create main layout
        main_layout.addWidget(tab_widget)  # Add the tab widget to main layout
        self.setLayout(main_layout)  # Set the layout for the main window

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())


"""
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTabWidget Example')

        # Create the tab widget
        tab_widget = QTabWidget()

        # Tab 1: Simple label
        tab1 = QWidget()
        tab1_layout = QLabel('This is Tab 1')
        tab1.setLayout(tab1_layout)

        # Tab 2: Another label
        tab2 = QWidget()
        tab2_layout = QLabel('This is Tab 2')
        tab2.setLayout(tab2_layout)

        # Add tabs to the widget
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        # Set the layout for the window
        self.setLayout(tab_widget)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
"""