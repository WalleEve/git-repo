from PyQt5.QtWidgets import QMainWindow, QTabWidget
from daily_expenses_tab import DailyExpensesTab
from admin import AdminTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cash+Guard")
        self.setGeometry(100, 100, 800, 600)

        # Create a tab widget
        self.tabs = QTabWidget()

        # Add tabs
        self.daily_expenses_tab = DailyExpensesTab()
        self.admin_tab = AdminTab()

        self.tabs.addTab(self.daily_expenses_tab, "Daily Expenses Log")
        self.tabs.addTab(self.admin_tab, "Admin")

        # Set the central widget
        self.setCentralWidget(self.tabs)