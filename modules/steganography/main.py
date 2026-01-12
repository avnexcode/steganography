import os
from utils import select_image_file, select_output_location, display_process
from modules.steganography import embed_lsb, extract_lsb
from modules.cryptography import encrypt_text, decrypt_text


def get_encryption_key(cipher_type):
    if cipher_type == "1":
        return int(input("Enter key (number): "))
    elif cipher_type == "2":
        return 13
    elif cipher_type == "3":
        return int(input("Enter key (number of columns): "))
    elif cipher_type == "4":
        return input("Enter key (string): ").strip()


def get_cipher_name(cipher_type):
    cipher_names = {"1": "Caesar", "2": "ROT13", "3": "Transposition", "4": "Vigenere"}
    return cipher_names.get(cipher_type, "Unknown")


def handle_encryption(cipher_type, mode):
    image_path = None
    if mode == "2":
        image_path = select_image_file("Select Image for Encryption")
        if not image_path or not os.path.exists(image_path):
            print("[✗] Invalid image file!")
            return False

    plaintext = input("\nEnter plaintext: ").strip()

    try:
        key = get_encryption_key(cipher_type)
        ciphertext, process = encrypt_text(plaintext, key, cipher_type)
        cipher_name = get_cipher_name(cipher_type)
    except ValueError:
        print("[✗] Key must be a number!")
        return False

    print(f"\n--- {cipher_name.upper()} ENCRYPTION RESULT ---")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    display_process(process)
    print(f"\nCiphertext: {ciphertext}")

    if mode == "2":
        output_path = select_output_location(image_path, suffix="-enc")
        if output_path:
            try:
                embed_lsb(image_path, ciphertext, output_path)
            except ValueError as e:
                print(f"[✗] Error: {e}")
                return False

    return True


def handle_decryption(cipher_type, mode):
    if mode == "2":
        image_path = select_image_file("Select Encrypted Image for Decryption")
        if not image_path or not os.path.exists(image_path):
            print("[✗] Invalid image file!")
            return False

        print("\n[*] Extracting message from image...")
        try:
            ciphertext = extract_lsb(image_path)
            print(f"[✓] Ciphertext successfully extracted: {ciphertext[:50]}...")
        except ValueError as e:
            print(f"[✗] Error: {e}")
            return False
    else:
        ciphertext = input("\nEnter ciphertext: ").strip()

    try:
        key = get_encryption_key(cipher_type)
        plaintext, process = decrypt_text(ciphertext, key, cipher_type)
        cipher_name = get_cipher_name(cipher_type)
    except ValueError:
        print("[✗] Key must be a number!")
        return False

    print(f"\n--- {cipher_name.upper()} DECRYPTION RESULT ---")
    print(f"Ciphertext: {ciphertext}")
    print(f"Key: {key}")
    display_process(process)
    print(f"\nPlaintext: {plaintext}")

    return True
