from cryptography.fernet import Fernet

def load_key():
    with open("C:/Users/user/Desktop/keylogger_project/secret.key", "rb") as f:
        return f.read()

def decrypt_line(encrypted_line, key):
    f = Fernet(key)
    try:
        return f.decrypt(encrypted_line.strip()).decode()
    except Exception as e:
        return f"[Decryption failed] {e}"

def main():
    key = load_key()
    with open("C:/Users/user/Desktop/keylogger_project/log.txt", "rb") as file:
        encrypted_lines = file.readlines()

    print("✅ Decrypted Logs:\n")
    for line in encrypted_lines:
        print(decrypt_line(line, key))

if __name__ == "__main__":
    main()
