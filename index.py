import os
from modules.steganography import handle_encryption, handle_decryption

from utils.display_cli import (
    display_header,
    display_cipher_menu,
    display_action_menu,
    display_output_mode_menu,
)


def handle_next_action():
    print("\n")
    print("--- NEXT ACTION ---")
    print("1. Continue")
    print("2. Clear terminal")

    next_action = input("\nChoose option (1/2): ").strip()

    if next_action == "2":
        os.system("cls" if os.name == "nt" else "clear")


def main():
    display_header()

    while True:
        menu_choice = display_cipher_menu()

        if menu_choice == "0":
            print("\n[✓] Thank you for using this application!")
            break

        if menu_choice not in ["1", "2", "3", "4"]:
            print("[✗] Invalid choice!")
            continue

        action = display_action_menu()
        if action not in ["1", "2"]:
            print("[✗] Invalid choice!")
            continue

        mode = display_output_mode_menu()
        if mode not in ["1", "2"]:
            print("[✗] Invalid choice!")
            continue

        if action == "1":
            handle_encryption(menu_choice, mode)
        else:
            handle_decryption(menu_choice, mode)

        handle_next_action()


if __name__ == "__main__":
    main()
