import string

uppercase: str = string.ascii_uppercase


import string

uppercase: str = string.ascii_uppercase


def caesarEncrypt(plaintext: str, key: int, show_process: bool = False):
    encrypt = ""
    plaintext_clean = plaintext.replace(" ", "").upper()
    process = []

    for letter in plaintext_clean:
        if letter in uppercase:
            p = uppercase.index(letter)
            shifted = (p + key) % 26
            encrypted_char = uppercase[shifted]
            encrypt += encrypted_char

            if show_process:
                process.append(
                    f"E({letter}) = ({p}+{key}) mod 26 = {shifted} → {encrypted_char}"
                )
        else:
            encrypt += letter

    return encrypt, process if show_process else encrypt


def caesarDecrypt(ciphertext: str, key: int, show_process: bool = False):
    decrypt = ""
    ciphertext_clean = ciphertext.upper()
    process = []

    for letter in ciphertext_clean:
        if letter in uppercase:
            c = uppercase.index(letter)
            shifted = (c - key) % 26
            decrypted_char = uppercase[shifted]
            decrypt += decrypted_char

            if show_process:
                process.append(
                    f"D({letter}) = ({c}-{key}) mod 26 = {shifted} → {decrypted_char}"
                )
        else:
            decrypt += letter

    return decrypt, process if show_process else decrypt


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


def menu_caesar():
    print("\n--- CAESAR CIPHER ---")
    pilihan = input("Pilih (1=Enkripsi, 2=Dekripsi): ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")
        key = int(input("Masukkan key (angka): "))

        ciphertext, process = caesarEncrypt(plaintext, key, show_process=True)

        print("\n--- PROSES ENKRIPSI ---")
        print(f"Rumus: E(p) = (p + k) mod 26")
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        print("\nProses per karakter:")
        for p in process:
            print(f"  {p}")
        print(f"\nCiphertext: {ciphertext}")

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = int(input("Masukkan key (angka): "))

        plaintext, process = caesarDecrypt(ciphertext, key, show_process=True)

        print("\n--- PROSES DEKRIPSI ---")
        print(f"Rumus: D(c) = (c - k) mod 26")
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: {key}")
        print("\nProses per karakter:")
        for p in process:
            print(f"  {p}")
        print(f"\nPlaintext: {plaintext}")


def menu_exhaustive():
    print("\n--- EXHAUSTIVE KEY SEARCH (CAESAR) ---")
    ciphertext = input("Masukkan ciphertext: ")

    print("\n--- HASIL PENCARIAN SEMUA KEY ---")
    results = exhaustiveKeySearch(ciphertext)
    for result in results:
        print(result)
