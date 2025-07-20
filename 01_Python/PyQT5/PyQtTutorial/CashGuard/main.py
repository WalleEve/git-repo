import sys
from ui.login import LoginWindow
from ui.main_window import MainWindow
from tabs.savings_log import SavingLog
from models.data_store import DataStore
from tabs.daily_expenses import DailyExpenses
from tabs.borrowings import BorrowingsTab
from tabs.admin.personal_tab import PersonalTab

from tabs.admin.user_tab import UserTab
from tabs.admin.account_tab import AccountTab

class CashGuardApp:
    def __init__(self):
        self.data_store = DataStore()  # Simulated data storage
        self.user_tab = UserTab(self.data_store)
        self.account_tab = AccountTab(self.data_store)
        self.personal_tab = PersonalTab(self.data_store)
        self.daily_expenses_tab = DailyExpenses(self.data_store)
        self.saving_log_tab = SavingLog(self.data_store)
        self.borrowings_tab = BorrowingsTab(self.data_store)

    def start(self):
        # Start the application by opening the login window
        login_window = LoginWindow(self)
        login_window.show()

    def authenticate_user(self, username, password):
        """Authenticate user based on username and password"""
        if self.user_tab.authenticate(username, password):
            print("Authentication successful!")
            self.open_main_window()
        else:
            print("Invalid username or password. Please try again.")

    def open_main_window(self):
        """Open the main application window after successful login"""
        main_window = MainWindow(self)
        main_window.show()

    def exit_app(self):
        """Exit the application gracefully"""
        print("Exiting the CashGuard application.")
        sys.exit()


if __name__ == "__main__":
    app = CashGuardApp()
    app.start()
