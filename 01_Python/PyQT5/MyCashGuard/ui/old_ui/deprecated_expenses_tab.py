### ui/expense_tab.py
# Module for the Daily Expense Tracking tab

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QDateEdit, QMessageBox
)
from PyQt5.QtCore import QDate

class ExpenseTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.layout = QVBoxLayout()
        self.tab = QWidget()

        
        # Daily Expense Log Section
        self.layout.addWidget(QLabel("Daily Expense Log:"))

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

        self.layout.addLayout(expense_layout)

        self.expense_table = QTableWidget(0, 4)
        self.expense_table.setHorizontalHeaderLabels(["Date", "Description", "Amount", "Payment Option"])
        self.layout.addWidget(self.expense_table)

        self.expense_total_label = QLabel("Total Expense: 0")
        self.layout.addWidget(self.expense_total_label)

        self.setLayout(self.layout)
         # Payment Reminders Section
        self.layout.addWidget(QLabel("Payment Reminders:"))

        reminder_layout = QHBoxLayout()
        self.reminder_desc_input = QLineEdit()
        self.reminder_desc_input.setPlaceholderText("Enter bill description")
        reminder_layout.addWidget(self.reminder_desc_input)

        self.reminder_date_input = QLineEdit()
        self.reminder_date_input.setPlaceholderText("Enter due date")
        reminder_layout.addWidget(self.reminder_date_input)

        self.add_reminder_button = QPushButton("Add Reminder")
        self.add_reminder_button.clicked.connect(self.add_reminder)
        reminder_layout.addWidget(self.add_reminder_button)

        self.layout.addLayout(reminder_layout)

        self.reminder_table = QTableWidget(0, 2)
        self.reminder_table.setHorizontalHeaderLabels(["Bill Description", "Due Date"])
        self.layout.addWidget(self.reminder_table)

        self.tab.setLayout(self.layout)

        self.load_expenses()

    def add_expense(self):
        date = self.expense_date_input.date().toString("yyyy-MM-dd")
        desc = self.expense_desc_input.text()
        amount = self.expense_amount_input.text()
        payment_option = self.payment_option_input.currentText()

        if date and desc and amount.isdigit():
            self.db_manager.add_expense(date, desc, int(amount), payment_option)
            self.load_expenses()
            self.expense_desc_input.clear()
            self.expense_amount_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter valid date, description, and numeric amount.")

    def load_expenses(self):
        self.expense_table.setRowCount(0)
        total = 0
        for expense in self.db_manager.get_expenses():
            row_count = self.expense_table.rowCount()
            self.expense_table.insertRow(row_count)
            self.expense_table.setItem(row_count, 0, QTableWidgetItem(expense["date"]))
            self.expense_table.setItem(row_count, 1, QTableWidgetItem(expense["description"]))
            self.expense_table.setItem(row_count, 2, QTableWidgetItem(str(expense["amount"])))
            self.expense_table.setItem(row_count, 3, QTableWidgetItem(expense["payment_option"]))
            total += expense["amount"]

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




