from .caesar import caesarEncrypt, caesarDecrypt


def rot13Encrypt(plaintext: str, show_process: bool = False):
    return caesarEncrypt(plaintext, 13, show_process)


def rot13Decrypt(ciphertext: str, show_process: bool = False):
    return caesarDecrypt(ciphertext, 13, show_process)


def menu_rot13():
    print("\n--- ROT13 CIPHER ---")
    pilihan = input("Pilih (1=Enkripsi, 2=Dekripsi): ")

    if pilihan == "1":
        plaintext = input("Masukkan plaintext: ")

        ciphertext, process = rot13Encrypt(plaintext, show_process=True)

        print("\n--- PROSES ENKRIPSI ---")
        print(f"Rumus: E(p) = (p + 13) mod 26")
        print(f"Plaintext: {plaintext}")
        print(f"Key: 13 (tetap)")
        print("\nProses per karakter (5 pertama):")
        for p in process[:5]:
            print(f"  {p}")
        if len(process) > 5:
            print(f"  ... dan {len(process)-5} karakter lainnya")
        print(f"\nCiphertext: {ciphertext}")

    elif pilihan == "2":
        ciphertext = input("Masukkan ciphertext: ")

        plaintext, process = rot13Decrypt(ciphertext, show_process=True)

        print("\n--- PROSES DEKRIPSI ---")
        print(f"Rumus: D(c) = (c - 13) mod 26")
        print(f"Ciphertext: {ciphertext}")
        print(f"Key: 13 (tetap)")
        print("\nProses per karakter (5 pertama):")
        for p in process[:5]:
            print(f"  {p}")
        if len(process) > 5:
            print(f"  ... dan {len(process)-5} karakter lainnya")
        print(f"\nPlaintext: {plaintext}")
