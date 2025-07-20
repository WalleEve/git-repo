# savings_log.py
import sqlite3
from PyQt5 import QtWidgets, QtCore

class SavingLog(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_db()
        self.init_ui()
        self.load_savings()

    def init_db(self):
        """Initialize SQLite database and create savings table if not exists"""
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS savings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL,
                date TEXT
            )
        """)
        self.conn.commit()

    def init_ui(self):
        self.setWindowTitle("Savings Log")
        self.resize(400, 350)

        # Widgets
        self.label = QtWidgets.QLabel("Log your savings:", self)

        self.desc_input = QtWidgets.QLineEdit(self)
        self.desc_input.setPlaceholderText("Savings Description")

        self.amount_input = QtWidgets.QLineEdit(self)
        self.amount_input.setPlaceholderText("Amount")
        self.amount_input.setValidator(QtWidgets.QDoubleValidator(0, 100000, 2))  # Only allows numbers

        self.add_button = QtWidgets.QPushButton("Add Saving", self)
        self.add_button.clicked.connect(self.add_saving)

        self.saving_list = QtWidgets.QListWidget(self)

        self.back_button = QtWidgets.QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.saving_list)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def load_savings(self):
        """Load savings from database and display in the list"""
        self.saving_list.clear()
        self.cursor.execute("SELECT description, amount, date FROM savings")
        for desc, amount, date in self.cursor.fetchall():
            self.saving_list.addItem(f"{desc} - ${amount} (Date: {date})")

    def add_saving(self):
        """Add saving to database and display it"""
        description = self.desc_input.text().strip()
        amount = self.amount_input.text().strip()

        if description and amount:
            self.cursor.execute("INSERT INTO savings (description, amount, date) VALUES (?, ?, DATE('now'))",
                                (description, float(amount)))
            self.conn.commit()
            self.load_savings()  # Refresh list
            self.desc_input.clear()
            self.amount_input.clear()
        else:
            QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter both description and amount.")

    def go_back(self):
        """Close this window and return to main menu"""
        self.main_window.show()
        self.close()

    def closeEvent(self, event):
        """Ensure database connection is closed properly"""
        self.conn.close()
        event.accept()
