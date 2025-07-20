from .user_tab import UserTab
from .account_tab import AccountTab
from .personal_tab import PersonalTab
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

class AdminTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Create sub-tabs for Admin
        self.admin_sub_tabs = QTabWidget()
        self.admin_sub_tabs.addTab(UserTab(), "User")
        self.admin_sub_tabs.addTab(AccountTab(), "Account")
        self.admin_sub_tabs.addTab(PersonalTab(), "Personal")

        layout.addWidget(self.admin_sub_tabs)
        self.setLayout(layout)