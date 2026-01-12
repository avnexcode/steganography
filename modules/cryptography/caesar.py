import string

uppercase: str = string.ascii_uppercase


def caesarEncrypt(plaintext: str, key: int):
    encrypt = ""
    plaintext_clean = plaintext.replace(" ", "").upper()

    for letter in plaintext_clean:
        if letter in uppercase:
            p = uppercase.index(letter)
            shifted = (p + key) % 26
            encrypted_char = uppercase[shifted]
            encrypt += encrypted_char

        else:
            encrypt += letter

    return encrypt


def caesarDecrypt(ciphertext: str, key: int):
    decrypt = ""
    ciphertext_clean = ciphertext.upper()

    for letter in ciphertext_clean:
        if letter in uppercase:
            c = uppercase.index(letter)
            shifted = (c - key) % 26
            decrypted_char = uppercase[shifted]
            decrypt += decrypted_char

        else:
            decrypt += letter

    return decrypt


def exhaustiveKeySearch(ciphertext: str):
    result = []
    ciphertext = ciphertext.upper()

    for shift in range(26):
        decrypt = ""
        for letter in ciphertext:
            if letter in uppercase:
                index = uppercase.index(letter)
                shifted_index = (index - shift) % 26
                decrypt += uppercase[shifted_index]
            else:
                decrypt += letter
        result.append(f"Key {shift:2d}: {decrypt}")

    return result


def menu_exhaustive():
    print("\n--- EXHAUSTIVE KEY SEARCH (CAESAR) ---")
    ciphertext = input("Masukkan ciphertext: ")

    print("\n--- HASIL PENCARIAN SEMUA KEY ---")
    results = exhaustiveKeySearch(ciphertext)
    for result in results:
        print(result)
