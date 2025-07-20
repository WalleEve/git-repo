from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt, QDate
from models.expenses_log import expenses_log

class DailyExpensesTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
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

        self.setLayout(layout)

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