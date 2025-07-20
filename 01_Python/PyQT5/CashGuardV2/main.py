
"""
cash_guard_project/
│
├── main.py                     # Entry point of the application
├── login_window.py             # Login window implementation
├── main_window.py              # Main window with tabs
├── daily_expenses_tab.py       # Daily Expenses tab implementation
├── admin_tab/                  # Admin tab and its sub-tabs
│   ├── __init__.py
│   ├── user_tab.py             # User tab implementation
│   ├── account_tab.py          # Account tab implementation
│   └── personal_tab.py         # Personal tab implementation
└── data/                       # Simulated data storage
    ├── __init__.py
    ├── expenses_log.py         # Expenses log data
    ├── user_data.py            # User data
    ├── account_data.py         # Account data
    └── personal_data.py        # Personal data
"""
import sys
from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Modern style
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())