from .caesar import caesarEncrypt, caesarDecrypt
from .rot13 import rot13Encrypt, rot13Decrypt
from .transposition import transposEncrypt, transposDecrypt
from .vigenere import vigenereEncrypt, vigenereDecrypt


def encrypt_text(plaintext, key, cipher_type):
    if cipher_type == "1":
        return caesarEncrypt(plaintext, key, show_process=True)
    elif cipher_type == "2":
        return rot13Encrypt(plaintext, show_process=True)
    elif cipher_type == "3":
        return transposEncrypt(plaintext, key, show_process=True)
    elif cipher_type == "4":
        return vigenereEncrypt(plaintext, key, show_process=True)


def decrypt_text(ciphertext, key, cipher_type):
    if cipher_type == "1":
        return caesarDecrypt(ciphertext, key, show_process=True)
    elif cipher_type == "2":
        return rot13Decrypt(ciphertext, show_process=True)
    elif cipher_type == "3":
        return transposDecrypt(ciphertext, key, show_process=True)
    elif cipher_type == "4":
        return vigenereDecrypt(ciphertext, key, show_process=True)
