# helpers.py
import re
import hashlib
from datetime import datetime

# Utility function to validate an email address using regex
def validate_email(email: str) -> bool:
    """Validate if the provided email address is in the correct format."""
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_regex, email))

# Utility function to validate a phone number (basic validation)
def validate_phone(phone: str) -> bool:
    """Validate if the provided phone number is in the correct format (xxx-xxx-xxxx)."""
    phone_regex = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(phone_regex, phone))

# Utility function to validate password strength
def validate_password(password: str) -> bool:
    """Validate if the password is strong enough (at least 8 characters, one digit, one uppercase, one lowercase)."""
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    return True

# Utility function to hash a password using SHA256
def hash_password(password: str) -> str:
    """Return the SHA256 hash of the given password."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Utility function to format a date (e.g., "YYYY-MM-DD")
def format_date(date_str: str) -> str:
    """Convert a date string from 'YYYY-MM-DD' format to a more readable format (e.g., 'January 1, 2025')."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return "Invalid date format"

# Utility function to check if a given account balance is sufficient
def has_sufficient_balance(account_balance: float, amount: float) -> bool:
    """Check if the account balance is sufficient for a withdrawal or transaction."""
    return account_balance >= amount

# Utility function to validate username (only alphanumeric characters and underscores)
def validate_username(username: str) -> bool:
    """Validate if the username contains only alphanumeric characters and underscores."""
    return bool(re.match(r"^[A-Za-z0-9_]+$", username))

# Utility function to log activities (could be useful for debugging or tracking)
def log_activity(activity: str) -> None:
    """Log the activity with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {activity}")

# Utility function to format account balance to two decimal places
def format_balance(balance: float) -> str:
    """Format account balance to two decimal places."""
    return f"${balance:.2f}"

# Example function to generate a unique user ID
def generate_user_id(username: str) -> str:
    """Generate a unique user ID based on username (you can also use a UUID generator here)."""
    return f"user_{hashlib.sha256(username.encode('utf-8')).hexdigest()[:8]}"

# Utility function to validate date of birth (must be in 'YYYY-MM-DD' format and over 18 years old)
def validate_dob(dob: str) -> bool:
    """Validate if the provided date of birth (DOB) is valid and user is over 18."""
    try:
        dob_obj = datetime.strptime(dob, "%Y-%m-%d")
        age = (datetime.now() - dob_obj).days // 365
        return age >= 18
    except ValueError:
        return False

# Utility function to check if a string is empty
def is_empty(string: str) -> bool:
    """Check if the given string is empty or contains only whitespaces."""
    return not bool(string.strip())

