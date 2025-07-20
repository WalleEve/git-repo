import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
    QMessageBox, QTabWidget, QFormLayout, QMainWindow, QDateEdit, QComboBox, 
    QTableWidget, QTableWidgetItem, QHeaderView, QCalendarWidget, QTextEdit, QDialog, QGridLayout
)
from PyQt5.QtCore import Qt, QDate

# Simulated Data Storage
expenses_log = []
user_data = {
    "phone": "1234567890",
    "email": "user@example.com",
    "password": "old_password"
}
account_data = []
personal_data = []

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

        # Frame 1: Expense Entry Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # Date (Calendar Popup)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())

        # Item
        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Enter item")

        # Summary
        self.summary_input = QLineEdit()
        self.summary_input.setPlaceholderText("Enter summary")

        # Payment Type (Dropdown)
        self.payment_type_input = QComboBox()
        self.payment_type_input.addItems(["Cash", "PhonePay", "GPay", "Online Banking App", "ATM Card"])

        # Amount
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount")

        # Add widgets to Frame 1
        frame1_layout.addRow("Date:", self.date_input)
        frame1_layout.addRow("Item:", self.item_input)
        frame1_layout.addRow("Summary:", self.summary_input)
        frame1_layout.addRow("Payment Type:", self.payment_type_input)
        frame1_layout.addRow("Amount:", self.amount_input)

        frame1.setLayout(frame1_layout)

        # Frame 2: Search Bar
        frame2 = QWidget()
        frame2_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by date (YYYY-MM-DD)")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_expenses)

        frame2_layout.addWidget(self.search_input)
        frame2_layout.addWidget(self.search_button)
        frame2.setLayout(frame2_layout)

        # Frame 3: Grid View (QTableWidget)
        self.expenses_table = QTableWidget()
        self.expenses_table.setColumnCount(5)
        self.expenses_table.setHorizontalHeaderLabels(["Date", "Item", "Summary", "Payment Type", "Amount"])
        self.expenses_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.expenses_table.setEditTriggers(QTableWidget.DoubleClicked)  # Enable editing

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.save_expenses)

        # Add frames and button to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        layout.addWidget(self.expenses_table)
        layout.addWidget(self.submit_button)

        self.daily_expenses_tab.setLayout(layout)

        # Load initial data into the table
        self.load_expenses()

    def load_expenses(self):
        """Load all expenses into the table."""
        self.expenses_table.setRowCount(len(expenses_log))
        for row, expense in enumerate(expenses_log):
            for col, value in enumerate(expense):
                item = QTableWidgetItem(str(value))
                if col == 0:  # Disable editing for the Date column
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.expenses_table.setItem(row, col, item)

    def search_expenses(self):
        """Filter expenses by date and display in the table."""
        search_date = self.search_input.text()
        filtered_expenses = [expense for expense in expenses_log if expense[0] == search_date]
        self.expenses_table.setRowCount(len(filtered_expenses))
        for row, expense in enumerate(filtered_expenses):
            for col, value in enumerate(expense):
                item = QTableWidgetItem(str(value))
                if col == 0:  # Disable editing for the Date column
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.expenses_table.setItem(row, col, item)

    def save_expenses(self):
        """Save or update expenses in the table."""
        # Collect data from the form
        date = self.date_input.date().toString("yyyy-MM-dd")
        item = self.item_input.text()
        summary = self.summary_input.text()
        payment_type = self.payment_type_input.currentText()
        amount = self.amount_input.text()

        # Validate input
        if not item or not summary or not amount:
            QMessageBox.warning(self, "Error", "All fields are required!")
            return

        # Add new expense to the log
        expenses_log.append([date, item, summary, payment_type, amount])

        # Reload the table
        self.load_expenses()

        # Clear the form
        self.item_input.clear()
        self.summary_input.clear()
        self.amount_input.clear()

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
        layout = QVBoxLayout()

        # Create sub-tabs for Admin
        self.admin_sub_tabs = QTabWidget()
        self.admin_sub_tabs.addTab(UserTab(), "User")
        self.admin_sub_tabs.addTab(AccountTab(), "Account")
        self.admin_sub_tabs.addTab(PersonalTab(), "Personal")

        layout.addWidget(self.admin_sub_tabs)
        self.admin_tab.setLayout(layout)

# Admin Tab: User Tab
class UserTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Phone and Email Update
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # Phone Update
        self.phone_label = QLabel(f"Registered Phone: ******{user_data['phone'][-4:]}")
        self.phone_update_button = QPushButton("Update Phone")
        self.phone_update_button.clicked.connect(self.update_phone)
        frame1_layout.addRow(self.phone_label, self.phone_update_button)

        # Email Update
        self.email_label = QLabel(f"Registered Email: ****{user_data['email'][-4:]}")
        self.email_update_button = QPushButton("Update Email")
        self.email_update_button.clicked.connect(self.update_email)
        frame1_layout.addRow(self.email_label, self.email_update_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Password Reset
        frame2 = QWidget()
        frame2_layout = QFormLayout()

        self.old_password_input = QLineEdit()
        self.old_password_input.setPlaceholderText("Enter old password")
        self.old_password_input.setEchoMode(QLineEdit.Password)

        self.new_password_input = QLineEdit()
        self.new_password_input.setPlaceholderText("Enter new password")
        self.new_password_input.setEchoMode(QLineEdit.Password)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm new password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.reset_button = QPushButton("Reset Password")
        self.reset_button.clicked.connect(self.reset_password)

        frame2_layout.addRow("Old Password:", self.old_password_input)
        frame2_layout.addRow("New Password:", self.new_password_input)
        frame2_layout.addRow("Confirm Password:", self.confirm_password_input)
        frame2_layout.addRow(self.reset_button)

        frame2.setLayout(frame2_layout)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        self.setLayout(layout)

    def update_phone(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Phone")
        dialog_layout = QFormLayout()

        self.old_phone_input = QLineEdit()
        self.old_phone_input.setPlaceholderText("Enter old phone number")

        self.new_phone_input = QLineEdit()
        self.new_phone_input.setPlaceholderText("Enter new phone number")

        self.update_phone_button = QPushButton("Update")
        self.update_phone_button.clicked.connect(lambda: self.validate_phone(dialog))

        dialog_layout.addRow("Old Phone:", self.old_phone_input)
        dialog_layout.addRow("New Phone:", self.new_phone_input)
        dialog_layout.addRow(self.update_phone_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def validate_phone(self, dialog):
        old_phone = self.old_phone_input.text()
        new_phone = self.new_phone_input.text()

        if old_phone == user_data["phone"]:
            user_data["phone"] = new_phone
            self.phone_label.setText(f"Registered Phone: ******{new_phone[-4:]}")
            QMessageBox.information(self, "Success", "Phone number updated successfully!")
            dialog.close()
        else:
            QMessageBox.warning(self, "Error", "Old phone number does not match!")

    def update_email(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Email")
        dialog_layout = QFormLayout()

        self.old_email_input = QLineEdit()
        self.old_email_input.setPlaceholderText("Enter old email")

        self.new_email_input = QLineEdit()
        self.new_email_input.setPlaceholderText("Enter new email")

        self.update_email_button = QPushButton("Update")
        self.update_email_button.clicked.connect(lambda: self.validate_email(dialog))

        dialog_layout.addRow("Old Email:", self.old_email_input)
        dialog_layout.addRow("New Email:", self.new_email_input)
        dialog_layout.addRow(self.update_email_button)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

    def validate_email(self, dialog):
        old_email = self.old_email_input.text()
        new_email = self.new_email_input.text()

        if old_email == user_data["email"]:
            user_data["email"] = new_email
            self.email_label.setText(f"Registered Email: ****{new_email[-4:]}")
            QMessageBox.information(self, "Success", "Email updated successfully!")
            dialog.close()
        else:
            QMessageBox.warning(self, "Error", "Old email does not match!")

    def reset_password(self):
        old_password = self.old_password_input.text()
        new_password = self.new_password_input.text()
        confirm_password = self.confirm_password_input.text()

        if old_password == user_data["password"]:
            if new_password == confirm_password:
                user_data["password"] = new_password
                QMessageBox.information(self, "Success", "Password reset successfully!")
            else:
                QMessageBox.warning(self, "Error", "New passwords do not match!")
        else:
            QMessageBox.warning(self, "Error", "Old password is incorrect!")

# Admin Tab: Account Tab
class AccountTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Account Details Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.bank_input = QLineEdit()
        self.ac_no_input = QLineEdit()
        self.ifsc_input = QLineEdit()
        self.reg_mob_input = QLineEdit()
        self.reg_email_input = QLineEdit()
        self.net_banking_user_input = QLineEdit()
        self.net_banking_password_input = QLineEdit()
        self.atm_card_no_input = QLineEdit()
        self.cvv_input = QLineEdit()
        self.pin_input = QLineEdit()
        self.upi_reg_mob_input = QLineEdit()
        self.upi_id_input = QLineEdit()
        self.upi_pin_input = QLineEdit()

        self.add_button = QPushButton("Add Account")
        self.add_button.clicked.connect(self.add_account)

        frame1_layout.addRow("Name:", self.name_input)
        frame1_layout.addRow("Bank:", self.bank_input)
        frame1_layout.addRow("Account No:", self.ac_no_input)
        frame1_layout.addRow("IFSC:", self.ifsc_input)
        frame1_layout.addRow("Registered Mobile:", self.reg_mob_input)
        frame1_layout.addRow("Registered Email:", self.reg_email_input)
        frame1_layout.addRow("Net Banking User:", self.net_banking_user_input)
        frame1_layout.addRow("Net Banking Password:", self.net_banking_password_input)
        frame1_layout.addRow("ATM Card No:", self.atm_card_no_input)
        frame1_layout.addRow("CVV:", self.cvv_input)
        frame1_layout.addRow("PIN:", self.pin_input)
        frame1_layout.addRow("UPI Registered Mobile:", self.upi_reg_mob_input)
        frame1_layout.addRow("UPI ID:", self.upi_id_input)
        frame1_layout.addRow("UPI PIN:", self.upi_pin_input)
        frame1_layout.addRow(self.add_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Grid View
        self.account_table = QTableWidget()
        self.account_table.setColumnCount(14)
        self.account_table.setHorizontalHeaderLabels([
            "Name", "Bank", "Account No", "IFSC", "Reg Mob", "Reg Email", "Net Banking User",
            "Net Banking Password", "ATM Card No", "CVV", "PIN", "UPI Reg Mob", "UPI ID", "UPI PIN"
        ])
        self.account_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(self.account_table)
        self.setLayout(layout)

    def add_account(self):
        account = [
            self.name_input.text(),
            self.bank_input.text(),
            self.ac_no_input.text(),
            self.ifsc_input.text(),
            self.reg_mob_input.text(),
            self.reg_email_input.text(),
            self.net_banking_user_input.text(),
            self.net_banking_password_input.text(),
            self.atm_card_no_input.text(),
            self.cvv_input.text(),
            self.pin_input.text(),
            self.upi_reg_mob_input.text(),
            self.upi_id_input.text(),
            self.upi_pin_input.text()
        ]
        account_data.append(account)
        self.load_accounts()

    def load_accounts(self):
        self.account_table.setRowCount(len(account_data))
        for row, account in enumerate(account_data):
            for col, value in enumerate(account):
                item = QTableWidgetItem(value)
                self.account_table.setItem(row, col, item)

# Admin Tab: Personal Tab
class PersonalTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Personal Details Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.dob_input = QDateEdit()
        self.dob_input.setCalendarPopup(True)
        self.address_input = QLineEdit()
        self.pan_input = QLineEdit()
        self.aadhar_input = QLineEdit()
        self.passport_input = QLineEdit()
        self.voter_id_input = QLineEdit()

        self.add_button = QPushButton("Add Personal Details")
        self.add_button.clicked.connect(self.add_personal_details)

        frame1_layout.addRow("Account Holder Name:", self.name_input)
        frame1_layout.addRow("Date of Birth:", self.dob_input)
        frame1_layout.addRow("Address:", self.address_input)
        frame1_layout.addRow("PAN:", self.pan_input)
        frame1_layout.addRow("AADHAR:", self.aadhar_input)
        frame1_layout.addRow("PASSPORT:", self.passport_input)
        frame1_layout.addRow("Voter ID:", self.voter_id_input)
        frame1_layout.addRow(self.add_button)

        frame1.setLayout(frame1_layout)

        # Frame 2: Grid View
        self.personal_table = QTableWidget()
        self.personal_table.setColumnCount(7)
        self.personal_table.setHorizontalHeaderLabels([
            "Name", "DOB", "Address", "PAN", "AADHAR", "PASSPORT", "Voter ID"
        ])
        self.personal_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add frames to the main layout
        layout.addWidget(frame1)
        layout.addWidget(self.personal_table)
        self.setLayout(layout)

    def add_personal_details(self):
        personal = [
            self.name_input.text(),
            self.dob_input.date().toString("yyyy-MM-dd"),
            self.address_input.text(),
            f"****{self.pan_input.text()[-4:]}",
            f"****{self.aadhar_input.text()[-4:]}",
            f"****{self.passport_input.text()[-4:]}",
            f"****{self.voter_id_input.text()[-4:]}"
        ]
        personal_data.append(personal)
        self.load_personal_details()

    def load_personal_details(self):
        self.personal_table.setRowCount(len(personal_data))
        for row, personal in enumerate(personal_data):
            for col, value in enumerate(personal):
                item = QTableWidgetItem(value)
                self.personal_table.setItem(row, col, item)

# Main Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Modern style
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())