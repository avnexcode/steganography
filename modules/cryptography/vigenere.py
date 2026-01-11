import string

uppercase: str = string.ascii_uppercase


def vigenereEncrypt(plaintext: str, key: str):
    encrypt = ""
    plaintext = plaintext.replace(" ", "").upper()
    key_index = 0

    for char in plaintext.upper():
        if char in uppercase:
            shift = uppercase.index(key.upper()[key_index % len(key)])
            new_index = (uppercase.index(char) + shift) % 26
            encrypt += uppercase[new_index]
            key_index += 1
        else:
            encrypt += char

    return encrypt


def vigenereDecrypt(cipher: str, key: str):
    decrypt = ""
    key_index = 0

    for char in cipher.upper():
        if char in uppercase:
            shift = uppercase.index(key.upper()[key_index % len(key)])
            new_index = (uppercase.index(char) - shift) % 26
            decrypt += uppercase[new_index]
            key_index += 1
        else:
            decrypt += char

    return decrypt


def menu_vigenere():
    print("\n--- VIGENERE CIPHER ---")
    pilihan = input("Pilih (1=Enkripsi, 2=Dekripsi): ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")
        key = input("Masukkan key (string): ")

        ciphertext, process = vigenereEncrypt(plaintext, key, show_process=True)

        print("\n--- PROSES ENKRIPSI ---")
        print(f"Rumus: E(p) = (p + k) mod 26")
        print(f"Plaintext: {plaintext}")
        print(f"Key: {key}")
        print("\nProses per karakter (10 pertama):")
        for p in process[:10]:
            print(f"  {p}")
        if len(process) > 10:
            print(f"  ... dan {len(process)-10} karakter lainnya")
        print(f"\nCiphertext: {ciphertext}")

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")
        key = input("Masukkan key (string): ")

        plaintext, process = vigenereDecrypt(ciphertext, key, show_process=True)

        print("\n--- PROSES DEKRIPSI ---")
        print(f"Rumus: D(c) = (c - k) mod 26")
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: {key}")
        print("\nProses per karakter (10 pertama):")
        for p in process[:10]:
            print(f"  {p}")
        if len(process) > 10:
            print(f"  ... dan {len(process)-10} karakter lainnya")
        print(f"\nPlaintext: {plaintext}")
