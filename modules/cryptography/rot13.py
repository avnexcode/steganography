from .caesar import caesarEncrypt, caesarDecrypt


def rot13Encrypt(plaintext: str):
    return caesarEncrypt(plaintext, 13)


def rot13Decrypt(ciphertext: str):
    return caesarDecrypt(ciphertext, 13)
