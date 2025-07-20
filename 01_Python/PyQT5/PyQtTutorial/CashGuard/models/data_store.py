# data_store.py
import json
import os

# Filepath for simulating data storage
DATA_FILE_PATH = "data_store.json"

# Sample data to simulate initial data
initial_data = {
    "users": {
        "user1": {"username": "johndoe", "password": "password123", "role": "admin"},
        "user2": {"username": "janedoe", "password": "password456", "role": "user"}
    },
    "accounts": {
        "user1": {"account_number": "1001", "balance": 1000.0},
        "user2": {"account_number": "1002", "balance": 1500.0}
    },
    "personal_details": {
        "user1": {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "dob": "1990-05-15",
            "phone": "123-456-7890"
        },
        "user2": {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "dob": "1992-07-20",
            "phone": "098-765-4321"
        }
    }
}

class DataStore:
    def __init__(self):
        self.load_data()

    def load_data(self):
        """Load data from the simulated storage (JSON file)."""
        if os.path.exists(DATA_FILE_PATH):
            with open(DATA_FILE_PATH, 'r') as file:
                self.data = json.load(file)
        else:
            # If the file doesn't exist, initialize with the sample data
            self.data = initial_data
            self.save_data()

    def save_data(self):
        """Save data to the simulated storage (JSON file)."""
        with open(DATA_FILE_PATH, 'w') as file:
            json.dump(self.data, file, indent=4)

    # User management
    def get_user(self, username):
        """Get user data by username."""
        return self.data["users"].get(username)

    def add_user(self, username, password, role):
        """Add a new user."""
        self.data["users"][username] = {"username": username, "password": password, "role": role}
        self.save_data()

    def update_user(self, username, password=None, role=None):
        """Update user details."""
        user = self.data["users"].get(username)
        if user:
            if password:
                user["password"] = password
            if role:
                user["role"] = role
            self.save_data()

    # Account management
    def get_account(self, username):
        """Get account details by username."""
        return self.data["accounts"].get(username)

    def add_account(self, username, account_number, balance):
        """Add a new account."""
        self.data["accounts"][username] = {"account_number": account_number, "balance": balance}
        self.save_data()

    def update_balance(self, username, balance):
        """Update account balance."""
        account = self.data["accounts"].get(username)
        if account:
            account["balance"] = balance
            self.save_data()

    # Personal details management
    def get_personal_details(self, username):
        """Get personal details by username."""
        return self.data["personal_details"].get(username)

    def update_personal_details(self, username, first_name=None, last_name=None, email=None, dob=None, phone=None):
        """Update personal details."""
        personal_details = self.data["personal_details"].get(username)
        if personal_details:
            if first_name:
                personal_details["first_name"] = first_name
            if last_name:
                personal_details["last_name"] = last_name
            if email:
                personal_details["email"] = email
            if dob:
                personal_details["dob"] = dob
            if phone:
                personal_details["phone"] = phone
            self.save_data()

    def reset_data(self):
        """Reset data to initial values."""
        self.data = initial_data
        self.save_data()


# Usage Example
if __name__ == "__main__":
    store = DataStore()

    # Adding a new user
    store.add_user("newuser", "newpassword", "user")
    
    # Updating a user's account balance
    store.update_balance("user1", 1200.0)

    # Retrieving user information
    user = store.get_user("user1")
    print(f"User: {user}")

    # Updating personal details for a user
    store.update_personal_details("user1", phone="555-555-5555")
    
    # Get updated personal details
    personal_details = store.get_personal_details("user1")
    print(f"Personal Details: {personal_details}")
