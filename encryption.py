from cryptography.fernet import Fernet

class AdvancedConstellationEncryption:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message: str) -> bytes:
        return self.cipher.encrypt(message.encode())

    def decrypt(self, encrypted_message: bytes) -> str:
        return self.cipher.decrypt(encrypted_message).decode()
