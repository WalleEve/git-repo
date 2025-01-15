from PyQt5.QtWidgets import QMainWindow, QMenuBar

class UserWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Dashboard")
        self.setGeometry(100, 100, 600, 400)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        menubar.addMenu('Sales')
        menubar.addMenu('Stocks')
