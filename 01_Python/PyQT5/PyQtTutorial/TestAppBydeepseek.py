import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QPushButton, QInputDialog
from PyQt5.QtCore import QStringListModel

class ListViewApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle('PyQt5 Model-View Example')
        self.setGeometry(100, 100, 400, 300)

        # Create a QVBoxLayout to manage the layout
        layout = QVBoxLayout()

        # Create a QStringListModel to hold the data
        self.model = QStringListModel()
        self.model.setStringList(['Item 1', 'Item 2', 'Item 3'])

        # Create a QListView to display the data
        self.list_view = QListView()
        self.list_view.setModel(self.model)

        # Create a QPushButton to add items
        self.add_button = QPushButton('Add Item')
        self.add_button.clicked.connect(self.add_item)

        # Create a QPushButton to remove items
        self.remove_button = QPushButton('Remove Item')
        self.remove_button.clicked.connect(self.remove_item)

        # Add the widgets to the layout
        layout.addWidget(self.list_view)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        # Set the layout for the main window
        self.setLayout(layout)

    def add_item(self):
        # Open an input dialog to get the new item text
        text, ok = QInputDialog.getText(self, 'Add Item', 'Enter new item:')
        if ok and text:
            # Add the new item to the model
            row = self.model.rowCount()
            self.model.insertRow(row)
            self.model.setData(self.model.index(row), text)

    def remove_item(self):
        # Get the selected index
        index = self.list_view.currentIndex()
        if index.isValid():
            # Remove the selected item from the model
            self.model.removeRow(index.row())

if __name__ == '__main__':
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = ListViewApp()
    window.show()

    # Execute the application
    sys.exit(app.exec_())