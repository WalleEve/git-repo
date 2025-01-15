import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox, QDateEdit
)
from PyQt5.QtCore import QDate

class MyCashGuard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyCashGuard - Personal Finance Management Tool")
        self.setGeometry(100, 100, 800, 600)

        # Create Tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Add sections as tabs
        self.tabs.addTab(self.create_expense_tab(), "Daily Expense Tracking")
        self.tabs.addTab(self.create_savings_tab(), "Savings & Investments")
        self.tabs.addTab(self.create_credit_tab(), "Credit/Debit Overview")

    def create_expense_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Daily Expense Log Section
        layout.addWidget(QLabel("Daily Expense Log:"))

        expense_layout = QHBoxLayout()

        self.expense_date_input = QDateEdit()
        self.expense_date_input.setCalendarPopup(True)
        self.expense_date_input.setDate(QDate.currentDate())
        expense_layout.addWidget(self.expense_date_input)

        self.expense_desc_input = QLineEdit()
        self.expense_desc_input.setPlaceholderText("Enter expense description")
        expense_layout.addWidget(self.expense_desc_input)

        self.expense_amount_input = QLineEdit()
        self.expense_amount_input.setPlaceholderText("Enter amount")
        expense_layout.addWidget(self.expense_amount_input)

        self.payment_option_input = QComboBox()
        self.payment_option_input.addItems(["card-1", "card-2", "card-3", "cash", "phone pay", "gPay"])
        expense_layout.addWidget(self.payment_option_input)

        self.add_expense_button = QPushButton("Add Expense")
        self.add_expense_button.clicked.connect(self.add_expense)
        expense_layout.addWidget(self.add_expense_button)

        layout.addLayout(expense_layout)

        self.expense_table = QTableWidget(0, 4)
        self.expense_table.setHorizontalHeaderLabels(["Date", "Description", "Amount", "Payment Option"])
        layout.addWidget(self.expense_table)

        self.expense_total_label = QLabel("Total Expense: 0")
        layout.addWidget(self.expense_total_label)

        # Payment Reminders Section
        layout.addWidget(QLabel("Payment Reminders:"))

        reminder_layout = QHBoxLayout()

        self.reminder_desc_input = QLineEdit()
        self.reminder_desc_input.setPlaceholderText("Enter bill description")
        reminder_layout.addWidget(self.reminder_desc_input)

        self.reminder_date_input = QDateEdit()
        self.reminder_date_input.setCalendarPopup(True)
        self.reminder_date_input.setDate(QDate.currentDate())
        reminder_layout.addWidget(self.reminder_date_input)

        self.add_reminder_button = QPushButton("Add Reminder")
        self.add_reminder_button.clicked.connect(self.add_reminder)
        reminder_layout.addWidget(self.add_reminder_button)

        layout.addLayout(reminder_layout)

        self.reminder_table = QTableWidget(0, 2)
        self.reminder_table.setHorizontalHeaderLabels(["Bill Description", "Due Date"])
        layout.addWidget(self.reminder_table)

        tab.setLayout(layout)
        return tab

    def add_expense(self):
        date = self.expense_date_input.date().toString("yyyy-MM-dd")
        desc = self.expense_desc_input.text()
        amount = self.expense_amount_input.text()
        payment_option = self.payment_option_input.currentText()

        if date and desc and amount.isdigit():
            row_count = self.expense_table.rowCount()
            self.expense_table.insertRow(row_count)
            self.expense_table.setItem(row_count, 0, QTableWidgetItem(date))
            self.expense_table.setItem(row_count, 1, QTableWidgetItem(desc))
            self.expense_table.setItem(row_count, 2, QTableWidgetItem(amount))
            self.expense_table.setItem(row_count, 3, QTableWidgetItem(payment_option))

            self.expense_date_input.setDate(QDate.currentDate())
            self.expense_desc_input.clear()
            self.expense_amount_input.clear()

            self.update_expense_total()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter valid date, description, and numeric amount.")

    def update_expense_total(self):
        total = 0
        for row in range(self.expense_table.rowCount()):
            total += int(self.expense_table.item(row, 2).text())
        self.expense_total_label.setText(f"Total Expense: {total}")

    def add_reminder(self):
        desc = self.reminder_desc_input.text()
        due_date = self.reminder_date_input.date().toString("yyyy-MM-dd")

        if desc and due_date:
            row_count = self.reminder_table.rowCount()
            self.reminder_table.insertRow(row_count)
            self.reminder_table.setItem(row_count, 0, QTableWidgetItem(desc))
            self.reminder_table.setItem(row_count, 1, QTableWidgetItem(due_date))

            self.reminder_desc_input.clear()
            self.reminder_date_input.setDate(QDate.currentDate())
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both bill description and due date.")

    def create_savings_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Savings Plans Section
        layout.addWidget(QLabel("Savings Goals:"))

        savings_layout = QHBoxLayout()
        self.savings_desc_input = QLineEdit()
        self.savings_desc_input.setPlaceholderText("Enter savings goal")
        savings_layout.addWidget(self.savings_desc_input)

        self.savings_target_input = QLineEdit()
        self.savings_target_input.setPlaceholderText("Enter target amount")
        savings_layout.addWidget(self.savings_target_input)

        self.add_savings_button = QPushButton("Add Savings Goal")
        self.add_savings_button.clicked.connect(self.add_savings_goal)
        savings_layout.addWidget(self.add_savings_button)

        layout.addLayout(savings_layout)

        self.savings_table = QTableWidget(0, 2)
        self.savings_table.setHorizontalHeaderLabels(["Goal", "Target Amount"])
        layout.addWidget(self.savings_table)

        # Investment Tracking Section
        layout.addWidget(QLabel("Investment Tracking:"))

        investment_layout = QHBoxLayout()
        self.investment_desc_input = QLineEdit()
        self.investment_desc_input.setPlaceholderText("Enter investment details")
        investment_layout.addWidget(self.investment_desc_input)

        self.investment_amount_input = QLineEdit()
        self.investment_amount_input.setPlaceholderText("Enter amount")
        investment_layout.addWidget(self.investment_amount_input)

        self.add_investment_button = QPushButton("Add Investment")
        self.add_investment_button.clicked.connect(self.add_investment)
        investment_layout.addWidget(self.add_investment_button)

        layout.addLayout(investment_layout)

        self.investment_table = QTableWidget(0, 2)
        self.investment_table.setHorizontalHeaderLabels(["Investment", "Amount"])
        layout.addWidget(self.investment_table)

        tab.setLayout(layout)
        return tab

    def add_savings_goal(self):
        goal = self.savings_desc_input.text()
        target = self.savings_target_input.text()
        if goal and target.isdigit():
            row_count = self.savings_table.rowCount()
            self.savings_table.insertRow(row_count)
            self.savings_table.setItem(row_count, 0, QTableWidgetItem(goal))
            self.savings_table.setItem(row_count, 1, QTableWidgetItem(target))
            self.savings_desc_input.clear()
            self.savings_target_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both savings goal and numeric target amount.")

    def add_investment(self):
        investment = self.investment_desc_input.text()
        amount = self.investment_amount_input.text()
        if investment and amount.isdigit():
            row_count = self.investment_table.rowCount()
            self.investment_table.insertRow(row_count)
            self.investment_table.setItem(row_count, 0, QTableWidgetItem(investment))
            self.investment_table.setItem(row_count, 1, QTableWidgetItem(amount))
            self.investment_desc_input.clear()
            self.investment_amount_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both investment details and numeric amount.")

    def create_credit_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Credit/Debit Overview Section
        layout.addWidget(QLabel("Credit/Debit Overview:"))

        credit_layout = QHBoxLayout()
        self.credit_desc_input = QLineEdit()
        self.credit_desc_input.setPlaceholderText("Enter credit/debit details")
        credit_layout.addWidget(self.credit_desc_input)

        self.credit_amount_input = QLineEdit()
        self.credit_amount_input.setPlaceholderText("Enter amount")
        credit_layout.addWidget(self.credit_amount_input)

        self.add_credit_button = QPushButton("Add Credit/Debit")
        self.add_credit_button.clicked.connect(self.add_credit)
        credit_layout.addWidget(self.add_credit_button)

        layout.addLayout(credit_layout)

        self.credit_table = QTableWidget(0, 2)
        self.credit_table.setHorizontalHeaderLabels(["Description", "Amount"])
        layout.addWidget(self.credit_table)

        tab.setLayout(layout)
        return tab

    def add_credit(self):
        desc = self.credit_desc_input.text()
        amount = self.credit_amount_input.text()
        if desc and amount.isdigit():
            row_count = self.credit_table.rowCount()
            self.credit_table.insertRow(row_count)
            self.credit_table.setItem(row_count, 0, QTableWidgetItem(desc))
            self.credit_table.setItem(row_count, 1, QTableWidgetItem(amount))
            self.credit_desc_input.clear()
            self.credit_amount_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter both description and numeric amount.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyCashGuard()
    window.show()
    sys.exit(app.exec_())


