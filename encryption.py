import random
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding

class AdvancedConstellationEncryption:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        self.public_key = self.private_key.public_key()

    def serialize_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def encrypt(self, plaintext):
        aes_key = random.randbytes(32)  # 256-bit AES key
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(random.randbytes(12)), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        tag = encryptor.tag
        encrypted_key = self.public_key.encrypt(
            aes_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256())
        )
        return base64.b64encode(encrypted_key + cipher.nonce + tag + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        encrypted_key = encrypted_data[:512]  # RSA encrypted AES key
        nonce = encrypted_data[512:524]  # AES GCM nonce
        tag = encrypted_data[524:540]  # AES GCM tag
        ciphertext = encrypted_data[540:]  # Encrypted payload
        aes_key = self.private_key.decrypt(
            encrypted_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256())
        )
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext
