from cryptography.fernet import Fernet


class CriptoQR:
    def __init__(self, key):
        self.key = key

    def __init__(self):
        self.key = self.create_key()

    def cipher(self, message, key):
        f = Fernet(key)
        message = str(message).encode()
        crypto = f.encrypt(message)
        return crypto

    def create_key(self):
        key = Fernet.generate_key()
        return key
