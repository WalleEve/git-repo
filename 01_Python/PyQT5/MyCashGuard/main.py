### main.py
# Main entry point of the application that initializes and runs the PyQt5 interface.

import sys
from PyQt5.QtWidgets import QApplication
from ui.expenses_tab import ExpenseTab
from ui.savings_tab import SavingsTab
from ui.credit_tab import CreditTab
from ui.admin_tab import AdminTab
from PyQt5.QtWidgets import QMainWindow, QTabWidget
from database.db_manager import DatabaseManager

class MyCashGuard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyCashGuard - Personal Finance Management Tool")
        self.setGeometry(100, 100, 800, 600)
        
        self.db_manager = DatabaseManager("mycashguard.db")

        # Create Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add sections as tabs
        self.expense_tab = ExpenseTab(self.db_manager)
        self.tabs.addTab(self.expense_tab, "Daily Expense Tracking")

        self.savings_tab = SavingsTab(self.db_manager)
        self.tabs.addTab(self.savings_tab, "Savings & Investments")

        self.credit_tab = CreditTab(self.db_manager)
        self.tabs.addTab(self.credit_tab, "Credit/Debit Overview")
        self.admin_tab = AdminTab(self.db_manager)
        self.tabs.addTab(self.admin_tab, "Admin")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyCashGuard()
    window.show()
    sys.exit(app.exec_())
