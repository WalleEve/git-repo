### main.py
# Main entry point of the application that initializes and runs the PyQt5 interface.

import sys
from PyQt5.QtWidgets import QApplication

from ui.admin_tab import AdminTab
from ui.savings_tab import SavingsTab

from PyQt5.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QDialog, QFormLayout, QLineEdit, \
    QPushButton, QMessageBox
from database.db_manager import DatabaseManager


class MyCashGuard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyCashGuard - Personal Finance Management Tool")
        self.setGeometry(100, 100, 800, 600)

        self.db_manager = DatabaseManager("mycashguard.db")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.tabs = QTabWidget()
        # self.general_tab = create_general_tab()
        self.admin_tab = QWidget()

        self.saving_tab = SavingsTab(self.db_manager)
        self.tabs.addTab(self.saving_tab, "Saving")

        self.admin_tab = AdminTab(self.db_manager)
        self.tabs.addTab(self.admin_tab, "Admin")

        self.tabs.tabBarClicked.connect(self.handle_tab_click)
        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def handle_tab_click(self, index):
        if self.tabs.tabText(index) == "Admin":
            login_dialog = AdminTab(self.db_manager)
            if login_dialog.exec_() == QDialog.Accepted:
                self.load_admin_tab()
            else:
                self.tabs.setCurrentIndex(0)

    def load_admin_tab(self):
        admin_layout = QVBoxLayout()
        admin_label = QLabel("Welcome to the Admin Panel!")
        admin_layout.addWidget(admin_label)
        self.admin_tab.setLayout(admin_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCashGuard()
    window.show()
    sys.exit(app.exec_())


