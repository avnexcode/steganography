import os
from tkinter import Tk, filedialog


def select_image_file(title: str = "Select Image File") -> str:
    print("\n--- SELECT INPUT METHOD ---")
    print("1. Open File Explorer")
    print("2. Manual Path Input")

    choice = input("Choose method (1/2): ").strip()

    if choice == "1":
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        file_path = filedialog.askopenfilename(
            title=title,
            filetypes=[
                ("All Image Files", "*.png *.bmp *.jpg *.jpeg *.gif *.tiff"),
                ("PNG Files", "*.png"),
                ("BMP Files", "*.bmp"),
                ("JPEG Files", "*.jpg *.jpeg"),
                ("All Files", "*.*"),
            ],
        )

        root.destroy()

        if file_path:
            print(f"[✓] File selected: {file_path}")
            return file_path
        else:
            print("[✗] No file selected!")
            return ""

    elif choice == "2":
        file_path = input("Enter image path: ").strip()
        return file_path
    else:
        print("[✗] Invalid choice!")
        return ""


def select_output_location(input_path: str, suffix: str = "-enc") -> str:
    print("\n--- SELECT OUTPUT LOCATION ---")
    print("1. Same as input location (automatic, will be saved as PNG)")
    print("2. Choose location with File Explorer")

    choice = input("Choose method (1/2): ").strip()

    if choice == "1":
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}{suffix}.png"
        print(f"[✓] Output will be saved at: {output_path}")
        return output_path

    elif choice == "2":
        root = Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        base_name = os.path.basename(input_path)
        name_without_ext = os.path.splitext(base_name)[0]
        default_name = f"{name_without_ext}{suffix}.png"

        output_path = filedialog.asksaveasfilename(
            title="Save Output Image (PNG Format)",
            initialfile=default_name,
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")],
        )

        root.destroy()

        if output_path:
            if not output_path.lower().endswith(".png"):
                output_path = os.path.splitext(output_path)[0] + ".png"
            print(f"[✓] Output will be saved at: {output_path}")
            return output_path
        else:
            print("[✗] No location selected!")
            return ""
    else:
        print("[✗] Invalid choice!")
        return ""
