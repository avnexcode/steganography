import os
from utils.image import select_image_file, select_output_location
from modules.steganography import embed_lsb, extract_lsb
from modules.cryptography import (
    caesarEncrypt,
    caesarDecrypt,
    rot13Encrypt,
    rot13Decrypt,
    transposEncrypt,
    transposDecrypt,
    vigenereEncrypt,
    vigenereDecrypt,
)


def main():
    print("\n" + "=" * 60)
    print(" " * 15 + "CRYPTOGRAPHY APPLICATION")
    print("=" * 60)

    while True:
        print("\n--- SELECT CIPHER ---")
        print("1. Caesar Cipher")
        print("2. ROT13 Cipher")
        print("3. Transposition Cipher")
        print("4. Vigenere Cipher")
        print("5. Exit")

        menu_choice = input("\nChoose cipher (1-5): ").strip()

        if menu_choice == "5":
            print("\n[✓] Thank you for using this application!")
            break

        if menu_choice not in ["1", "2", "3", "4"]:
            print("[✗] Invalid choice!")
            continue

        # Select action
        print("\n--- SELECT ACTION ---")
        print("1. Encryption")
        print("2. Decryption")

        action = input("Choose action (1/2): ").strip()

        if action not in ["1", "2"]:
            print("[✗] Invalid choice!")
            continue

        # Select output mode
        print("\n--- SELECT OUTPUT MODE ---")
        print("1. Text")
        print("2. LSB (Steganography)")

        mode = input("Choose mode (1/2): ").strip()

        if mode not in ["1", "2"]:
            print("[✗] Invalid choice!")
            continue

        # Encryption process
        if action == "1":
            if mode == "2":  # Image mode
                image_path = select_image_file("Select Image for Encryption")
                if not image_path or not os.path.exists(image_path):
                    print("[✗] Invalid image file!")
                    continue

            plaintext = input("\nEnter plaintext: ").strip()

            # Get key based on cipher type
            if menu_choice == "1":  # Caesar
                try:
                    key = int(input("Enter key (number): "))
                    ciphertext, process = caesarEncrypt(
                        plaintext, key, show_process=True
                    )
                    cipher_name = "Caesar"
                except ValueError:
                    print("[✗] Key must be a number!")
                    continue

            elif menu_choice == "2":  # ROT13
                key = 13
                ciphertext, process = rot13Encrypt(plaintext, show_process=True)
                cipher_name = "ROT13"

            elif menu_choice == "3":  # Transposition
                try:
                    key = int(input("Enter key (number of columns): "))
                    ciphertext, process = transposEncrypt(
                        plaintext, key, show_process=True
                    )
                    cipher_name = "Transposition"
                except ValueError:
                    print("[✗] Key must be a number!")
                    continue

            elif menu_choice == "4":  # Vigenere
                key = input("Enter key (string): ").strip()
                ciphertext, process = vigenereEncrypt(plaintext, key, show_process=True)
                cipher_name = "Vigenere"

            print(f"\n--- {cipher_name.upper()} ENCRYPTION RESULT ---")
            print(f"Plaintext: {plaintext}")
            print(f"Key: {key}")

            if process and len(process) > 0:
                print("\nProcess (first 5 characters):")
                for p in process[:5]:
                    print(f"  {p}")
                if len(process) > 5:
                    print(f"  ... and {len(process)-5} more characters")

            print(f"\nCiphertext: {ciphertext}")

            # Handle output mode
            if mode == "2":  # Embed to image
                output_path = select_output_location(image_path, suffix="-enc")
                if output_path:
                    try:
                        embed_lsb(image_path, ciphertext, output_path)
                    except ValueError as e:
                        print(f"[✗] Error: {e}")

        # Decryption process
        else:  # action == "2"
            if mode == "2":  # Extract from image
                image_path = select_image_file("Select Encrypted Image for Decryption")
                if not image_path or not os.path.exists(image_path):
                    print("[✗] Invalid image file!")
                    continue

                print("\n[*] Extracting message from image...")
                try:
                    ciphertext = extract_lsb(image_path)
                    print(
                        f"[✓] Ciphertext successfully extracted: {ciphertext[:50]}..."
                    )
                except ValueError as e:
                    print(f"[✗] Error: {e}")
                    continue
            else:  # String mode
                ciphertext = input("\nEnter ciphertext: ").strip()

            # Get key and decrypt based on cipher type
            if menu_choice == "1":  # Caesar
                try:
                    key = int(input("Enter key (number): "))
                    plaintext, process = caesarDecrypt(
                        ciphertext, key, show_process=True
                    )
                    cipher_name = "Caesar"
                except ValueError:
                    print("[✗] Key must be a number!")
                    continue

            elif menu_choice == "2":  # ROT13
                key = 13
                plaintext, process = rot13Decrypt(ciphertext, show_process=True)
                cipher_name = "ROT13"

            elif menu_choice == "3":  # Transposition
                try:
                    key = int(input("Enter key (number of columns): "))
                    plaintext, process = transposDecrypt(
                        ciphertext, key, show_process=True
                    )
                    cipher_name = "Transposition"
                except ValueError:
                    print("[✗] Key must be a number!")
                    continue

            elif menu_choice == "4":  # Vigenere
                key = input("Enter key (string): ").strip()
                plaintext, process = vigenereDecrypt(ciphertext, key, show_process=True)
                cipher_name = "Vigenere"

            print(f"\n--- {cipher_name.upper()} DECRYPTION RESULT ---")
            print(f"Ciphertext: {ciphertext}")
            print(f"Key: {key}")

            if process and len(process) > 0:
                print("\nProcess (first 5 characters):")
                for p in process[:5]:
                    print(f"  {p}")
                if len(process) > 5:
                    print(f"  ... and {len(process)-5} more characters")

            print(f"\nPlaintext: {plaintext}")

        # Ask user what to do next
        print("\n" + "-" * 60)
        print("--- NEXT ACTION ---")
        print("1. Continue")
        print("2. Clear terminal")

        next_action = input("\nChoose option (1/2): ").strip()

        if next_action == "2":
            # Clear terminal
            os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
