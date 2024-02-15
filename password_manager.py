from cryptography.fernet import Fernet
import random
import string

# A key needs to be Generated to instantiate a Fernet object
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(10))
    return password

def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()

def save_password(app_name, user_name, password, file='passwords.txt'):
    encrypted_password = encrypt_password(password)
    with open(file, "a") as f:
        f.write(f"{app_name}|{user_name}|{encrypted_password}\n")

def get_password(app_name, file='passwords.txt'):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    stored_app_name, user_name, encrypted_password = parts
                    if stored_app_name == app_name:
                        return user_name, decrypt_password(encrypted_password)
        return None, None
    except FileNotFoundError:
        return None, None

def update_password(app_name, user_name, old_password, new_password, file='passwords.txt'):
    new_lines = []
    with open(file, "r+") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split('|')
            if len(parts) == 3:
                stored_app_name, stored_user_name, encrypted_password = parts
                if stored_app_name == app_name and stored_user_name == user_name:
                    if decrypt_password(encrypted_password) == old_password:
                        new_lines.append(f"{app_name}|{user_name}|{encrypt_password(new_password)}\n")
                    else:
                        return "Error: Old password does not match."
                else:
                    new_lines.append(line)
        f.seek(0)
        f.truncate()
        f.writelines(new_lines)
    return "Success: Password updated successfully."