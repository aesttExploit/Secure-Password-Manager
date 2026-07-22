import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


def generate_key(master_password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )

    return base64.urlsafe_b64encode(
        kdf.derive(master_password.encode())
    )


def encrypt_password(password, master_password, salt):

    key = generate_key(master_password, salt)

    return Fernet(key).encrypt(
        password.encode()
    ).decode()


def decrypt_password(encrypted_password, master_password, salt):

    key = generate_key(master_password, salt)

    return Fernet(key).decrypt(
        encrypted_password.encode()
    ).decode()
   