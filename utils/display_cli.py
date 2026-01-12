def display_header():
    print("\n" + "=" * 30)
    print(" " * 3 + "CRYPTOGRAPHY APPLICATION")
    print("=" * 30)


def display_cipher_menu():
    print("\n--- SELECT CIPHER ---")
    print("1. Caesar Cipher")
    print("2. ROT13 Cipher")
    print("3. Transposition Cipher")
    print("4. Vigenere Cipher")
    print("0. Exit")
    return input("\nChoose cipher (0-4): ").strip()


def display_action_menu():
    print("\n--- SELECT ACTION ---")
    print("1. Encryption")
    print("2. Decryption")
    return input("Choose action (1/2): ").strip()


def display_output_mode_menu():
    print("\n--- SELECT OUTPUT MODE ---")
    print("1. Text")
    print("2. LSB (Steganography)")
    return input("Choose mode (1/2): ").strip()
