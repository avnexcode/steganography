import string

uppercase: str = string.ascii_uppercase


def vigenereEncrypt(plaintext: str, key: str):
    encrypt = ""
    plaintext_clean = plaintext.replace(" ", "").upper()
    key_upper = key.upper()
    key_index = 0

    for index, char in enumerate(plaintext_clean):
        if char in uppercase:
            key_char = key_upper[key_index % len(key_upper)]
            shift = uppercase.index(key_char)
            char_index = uppercase.index(char)
            new_index = (char_index + shift) % 26
            encrypted_char = uppercase[new_index]

            encrypt += encrypted_char
            key_index += 1
        else:
            encrypt += char

    return encrypt


def vigenereDecrypt(ciphertext: str, key: str):
    decrypt = ""
    cipher_clean = ciphertext.upper()
    key_upper = key.upper()
    key_index = 0

    for index, char in enumerate(cipher_clean):
        if char in uppercase:
            key_char = key_upper[key_index % len(key_upper)]
            shift = uppercase.index(key_char)
            char_index = uppercase.index(char)
            new_index = (char_index - shift) % 26
            decrypted_char = uppercase[new_index]

            decrypt += decrypted_char
            key_index += 1
        else:
            decrypt += char

    return decrypt
