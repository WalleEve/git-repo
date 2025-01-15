from PyQt5.QtWidgets import QMainWindow, QMenuBar

class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admin Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        menubar.addMenu('Sales Details')
        menubar.addMenu('Stock Details')
        menubar.addMenu('Stock Entry')
        menubar.addMenu('User Management')
        menubar.addMenu('Reports')
        menubar.addMenu('Help')
        
