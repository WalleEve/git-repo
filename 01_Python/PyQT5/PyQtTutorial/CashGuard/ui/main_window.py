# main_window.py
'''
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Main Window")
        self.resize(400, 200)

        # Create Widgets
        self.welcome_label = QtWidgets.QLabel(f"Welcome, {self.username}!", self)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)

        self.logout_button = QtWidgets.QPushButton("Logout", self)
        self.logout_button.clicked.connect(self.handle_logout)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.welcome_label)
        layout.addWidget(self.logout_button)

        # Central Widget
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_logout(self):
        from login_window import LoginWindow  # Import login window to switch back
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()  # Close the main window when logging out
'''

import sys
from PyQt5 import QtWidgets
from daily_expenses import DailyExpenses

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Expense Tracker")
        self.resize(300, 200)

        self.label = QtWidgets.QLabel("Welcome to Expense Tracker", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.daily_expenses_button = QtWidgets.QPushButton("Daily Expenses", self)
        self.daily_expenses_button.clicked.connect(self.open_daily_expenses)

        self.exit_button = QtWidgets.QPushButton("Exit", self)
        self.exit_button.clicked.connect(QtWidgets.qApp.quit)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.daily_expenses_button)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def open_daily_expenses(self):
        """Open the Daily Expenses window"""
        self.daily_expenses_window = DailyExpenses(self)
        self.daily_expenses_window.show()
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
