
### ui/savings_tab.py
# Module for the Daily Savings Tracking tab

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QPushButton, QLineEdit, QDateEdit, QMessageBox
)
from PyQt5.QtCore import QDate


class SavingsTab(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.layout = QVBoxLayout()

        # Savings Goals Section
        self.layout.addWidget(QLabel("Savings Goals:"))

        savings_layout = QHBoxLayout()

        self.savings_date_input = QDateEdit()
        self.savings_date_input.setCalendarPopup(True)
        self.savings_date_input.setDate(QDate.currentDate())
        savings_layout.addWidget(self.savings_date_input)

        self.savings_desc_input = QLineEdit()
        self.savings_desc_input.setPlaceholderText("Enter savings description")
        savings_layout.addWidget(self.savings_desc_input)

        self.savings_target_input = QLineEdit()
        self.savings_target_input.setPlaceholderText("Enter target amount")
        savings_layout.addWidget(self.savings_target_input)

        self.savings_current_input = QLineEdit()
        self.savings_current_input.setPlaceholderText("Enter current amount")
        savings_layout.addWidget(self.savings_current_input)

        self.add_savings_button = QPushButton("Add Savings")
        self.add_savings_button.clicked.connect(self.add_savings)
        savings_layout.addWidget(self.add_savings_button)

        self.layout.addLayout(savings_layout)

        self.savings_table = QTableWidget(0, 4)
        self.savings_table.setHorizontalHeaderLabels(["Date", "Description", "Target", "Current"])
        self.layout.addWidget(self.savings_table)

        self.savings_total_label = QLabel("Total Saved: 0")
        self.layout.addWidget(self.savings_total_label)

        self.setLayout(self.layout)

        self.load_savings()

    def add_savings(self):
        date = self.savings_date_input.date().toString("yyyy-MM-dd")
        desc = self.savings_desc_input.text()
        target = self.savings_target_input.text()
        current = self.savings_current_input.text()

        if date and desc and target.isdigit() and current.isdigit():
            self.db_manager.add_savings(date, desc, int(target), int(current))
            self.load_savings()
            self.savings_desc_input.clear()
            self.savings_target_input.clear()
            self.savings_current_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter valid data for all fields.")

    def load_savings(self):
        self.savings_table.setRowCount(0)
        total = 0
        for savings in self.db_manager.get_savings():
            row_count = self.savings_table.rowCount()
            self.savings_table.insertRow(row_count)
            self.savings_table.setItem(row_count, 0, QTableWidgetItem(savings["date"]))
            self.savings_table.setItem(row_count, 1, QTableWidgetItem(savings["description"]))
            self.savings_table.setItem(row_count, 2, QTableWidgetItem(str(savings["target"])))
            self.savings_table.setItem(row_count, 3, QTableWidgetItem(str(savings["current"])))
            total += savings["current"]

        self.savings_total_label.setText(f"Total Saved: {total}")


