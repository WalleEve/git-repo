from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QFormLayout, QDateEdit, QComboBox, QHBoxLayout,QPushButton
                    , QTableWidget, QTableWidgetItem, QMessageBox,  QDateTimeEdit, QLineEdit,)
import sqlite3

# Simulated Data Storage for Borrowings
borrowings_log = []

# Borrowings Tab UI
class BorrowingsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Frame 1: Borrowing Entry Form
        frame1 = QWidget()
        frame1_layout = QFormLayout()

        # Date (Calendar Popup)
        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDateTimeEdit.currentDate())

        # Borrower Name
        self.borrower_name_input = QLineEdit()
        self.borrower_name_input.setPlaceholderText("Enter borrower's name")

        # Item Borrowed
        self.item_input = QLineEdit()
        self.item_input.setPlaceholderText("Enter borrowed item")

        # Amount Borrowed (Optional)
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Enter amount borrowed (optional)")

        # Borrowing Type (Dropdown)
        self.borrowing_type_input = QComboBox()
        self.borrowing_type_input.addItems(["Loan", "Gift", "Rent"])

        # Add widgets to Frame 1
        frame1_layout.addRow("Date:", self.date_input)
        frame1_layout.addRow("Borrower's Name:", self.borrower_name_input)
        frame1_layout.addRow("Item Borrowed:", self.item_input)
        frame1_layout.addRow("Amount Borrowed:", self.amount_input)
        frame1_layout.addRow("Borrowing Type:", self.borrowing_type_input)

        frame1.setLayout(frame1_layout)

        # Frame 2: Search Bar
        frame2 = QWidget()
        frame2_layout = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by date (YYYY-MM-DD) or borrower name")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_borrowings)

        frame2_layout.addWidget(self.search_input)
        frame2_layout.addWidget(self.search_button)
        frame2.setLayout(frame2_layout)

        # Frame 3: Grid View (QTableWidget)
        self.borrowings_table = QTableWidget()
        self.borrowings_table.setColumnCount(5)
        self.borrowings_table.setHorizontalHeaderLabels(["Date", "Borrower", "Item", "Amount", "Type"])
        self.borrowings_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.borrowings_table.setEditTriggers(QTableWidget.DoubleClicked)  # Enable editing

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.save_borrowing)

        # Add frames and button to the main layout
        layout.addWidget(frame1)
        layout.addWidget(frame2)
        layout.addWidget(self.borrowings_table)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

        # Load initial data into the table
        self.load_borrowings()

    def load_borrowings(self):
        """Load all borrowings into the table."""
        self.borrowings_table.setRowCount(len(borrowings_log))
        for row, borrowing in enumerate(borrowings_log):
            for col, value in enumerate(borrowing):
                item = QTableWidgetItem(str(value))
                if col == 0:  # Disable editing for the Date column
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.borrowings_table.setItem(row, col, item)

    def search_borrowings(self):
        """Filter borrowings by date or borrower name and display in the table."""
        search_text = self.search_input.text().lower()
        filtered_borrowings = [
            borrowing for borrowing in borrowings_log if search_text in borrowing[0].lower() or search_text in borrowing[1].lower()
        ]
        self.borrowings_table.setRowCount(len(filtered_borrowings))
        for row, borrowing in enumerate(filtered_borrowings):
            for col, value in enumerate(borrowing):
                item = QTableWidgetItem(str(value))
                if col == 0:  # Disable editing for the Date column
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.borrowings_table.setItem(row, col, item)

    def save_borrowing(self):
        """Save or update a borrowing in the table."""
        # Collect data from the form
        date = self.date_input.date().toString("yyyy-MM-dd")
        borrower_name = self.borrower_name_input.text()
        item = self.item_input.text()
        amount = self.amount_input.text()
        borrowing_type = self.borrowing_type_input.currentText()

        # Validate input
        if not borrower_name or not item:
            QMessageBox.warning(self, "Error", "Borrower's name and borrowed item are required!")
            return

        # Add new borrowing to the log
        borrowings_log.append([date, borrower_name, item, amount, borrowing_type])

        # Reload the table
        self.load_borrowings()

        # Clear the form
        self.borrower_name_input.clear()
        self.item_input.clear()
        self.amount_input.clear()
