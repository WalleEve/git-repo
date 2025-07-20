import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QTabWidget, QTextEdit, QFormLayout, QMainWindow
)
from PyQt5.QtCore import Qt

# Login Window
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 300, 150)

        # Layout
        layout = QVBoxLayout()

        # Username field
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter username")

        # Password field
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        # Add widgets to layout
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def login(self):
        # Hardcoded credentials for demonstration
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            self.close()  # Close the login window
            self.main_window = MainWindow()  # Open the main window
            self.main_window.show()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

# Main Window with Tabs
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cash+Guard")
        self.setGeometry(100, 100, 800, 600)

        # Create a tab widget
        self.tabs = QTabWidget()

        # Add tabs
        self.daily_expenses_tab = QWidget()
        self.saving_log_tab = QWidget()
        self.borrowings_log_tab = QWidget()
        self.admin_tab = QWidget()

        self.tabs.addTab(self.daily_expenses_tab, "Daily Expenses Log")
        self.tabs.addTab(self.saving_log_tab, "Saving Log")
        self.tabs.addTab(self.borrowings_log_tab, "Borrowings Log")
        self.tabs.addTab(self.admin_tab, "Admin")

        # Set up each tab
        self.setup_daily_expenses_tab()
        self.setup_saving_log_tab()
        self.setup_borrowings_log_tab()
        self.setup_admin_tab()

        # Set the central widget
        self.setCentralWidget(self.tabs)

    def setup_daily_expenses_tab(self):
        layout = QVBoxLayout()
        self.daily_expenses_log = QTextEdit()
        self.daily_expenses_log.setPlaceholderText("Enter daily expenses here...")
        layout.addWidget(self.daily_expenses_log)
        self.daily_expenses_tab.setLayout(layout)

    def setup_saving_log_tab(self):
        layout = QVBoxLayout()
        self.saving_log = QTextEdit()
        self.saving_log.setPlaceholderText("Enter savings details here...")
        layout.addWidget(self.saving_log)
        self.saving_log_tab.setLayout(layout)

    def setup_borrowings_log_tab(self):
        layout = QVBoxLayout()
        self.borrowings_log = QTextEdit()
        self.borrowings_log.setPlaceholderText("Enter borrowings details here...")
        layout.addWidget(self.borrowings_log)
        self.borrowings_log_tab.setLayout(layout)

    def setup_admin_tab(self):
        layout = QFormLayout()
        self.admin_username_input = QLineEdit()
        self.admin_password_input = QLineEdit()
        self.admin_password_input.setEchoMode(QLineEdit.Password)
        self.admin_save_button = QPushButton("Save Admin Settings")

        layout.addRow("Admin Username:", self.admin_username_input)
        layout.addRow("Admin Password:", self.admin_password_input)
        layout.addRow(self.admin_save_button)

        self.admin_tab.setLayout(layout)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Show the login window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())