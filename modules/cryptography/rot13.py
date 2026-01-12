from .caesar import caesarEncrypt, caesarDecrypt


def rot13Encrypt(plaintext: str, show_process: bool = False):
    return caesarEncrypt(plaintext, 13, show_process)


def rot13Decrypt(ciphertext: str, show_process: bool = False):
    return caesarDecrypt(ciphertext, 13, show_process)
