from cryptography.fernet import Fernet
from config.settings import ENCRYPTION_KEY

def encrypt_data(data):
    if isinstance(data, str):
        data = data.encode()  # Convert to bytes if not already
    cipher = Fernet(ENCRYPTION_KEY)
    return cipher.encrypt(data)

def decrypt_data(encrypted_data):
    if isinstance(encrypted_data, memoryview):
        encrypted_data = encrypted_data.tobytes()
    cipher = Fernet(ENCRYPTION_KEY)
    return cipher.decrypt(encrypted_data)

