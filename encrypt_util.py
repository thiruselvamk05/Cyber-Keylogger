from cryptography.fernet import Fernet
import os

KEY_PATH = r"C:\Users\user\Desktop\keylogger_project\secret.key"

def write_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)
    print(f"✅ Key saved to: {KEY_PATH}")

def load_key():
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError(f"❌ secret.key not found at: {KEY_PATH}")
    return open(KEY_PATH, "rb").read()

def encrypt_message(message):
    key = load_key()
    return Fernet(key).encrypt(message.encode())

def decrypt_message(encrypted_message):
    key = load_key()
    return Fernet(key).decrypt(encrypted_message).decode()

if __name__ == "__main__":
    write_key()
