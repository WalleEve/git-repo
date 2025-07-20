from PyQt5 import QtWidgets
import sqlite3

class DailyExpenses(QtWidgets.QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.init_db()
        self.init_ui()
        self.load_expenses()

    def init_db(self):
        """Initialize SQLite database and create table if not exists"""
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL,
                category TEXT
            )
        """)
        self.conn.commit()

    def init_ui(self):
        self.setWindowTitle("Daily Expenses")
        self.resize(400, 350)

        # Widgets
        self.label = QtWidgets.QLabel("Enter your daily expenses:", self)

        self.desc_input = QtWidgets.QLineEdit(self)
        self.desc_input.setPlaceholderText("Expense Description")

        self.amount_input = QtWidgets.QLineEdit(self)
        self.amount_input.setPlaceholderText("Amount")
        self.amount_input.setValidator(QtWidgets.QDoubleValidator(0, 100000, 2))  # Only allows numbers

        # Category Dropdown
        self.category_dropdown = QtWidgets.QComboBox(self)
        self.category_dropdown.addItems(["Food", "Transport", "Shopping", "Bills", "Others"])

        self.add_button = QtWidgets.QPushButton("Add Expense", self)
        self.add_button.clicked.connect(self.add_expense)

        self.expense_list = QtWidgets.QListWidget(self)

        self.back_button = QtWidgets.QPushButton("Back", self)
        self.back_button.clicked.connect(self.go_back)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.desc_input)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.category_dropdown)
        layout.addWidget(self.add_button)
        layout.addWidget(self.expense_list)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def load_expenses(self):
        """Load expenses from database and display in the list"""
        self.expense_list.clear()
        self.cursor.execute("SELECT description, amount, category FROM expenses")
        for desc, amount, category in self.cursor.fetchall():
            self.expense_list.addItem(f"{desc} - ${amount} ({category})")

    def add_expense(self):
        """Add expense to database and display it"""
        description = self.desc_input.text().strip()
        amount = self.amount_input.text().strip()
        category = self.category_dropdown.currentText()

        if description and amount:
            self.cursor.execute("INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)",
                                (description, float(amount), category))
            self.conn.commit()
            self.load_expenses()  # Refresh list
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
