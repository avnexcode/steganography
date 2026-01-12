import os
from PIL import Image
from utils.string import string_to_binary, binary_to_string


def embed_lsb(image_path: str, message: str, output_path: str):
    try:
        img = Image.open(image_path)
        input_format = img.format
        print(f"[i] Input image format: {input_format}")
    except Exception as e:
        raise ValueError(f"Failed to open image: {e}")

    if img.mode != "RGB":
        img = img.convert("RGB")

    pixels = list(img.getdata())
    width, height = img.size

    message_with_delimiter = message + "###END###"
    binary_message = string_to_binary(message_with_delimiter)

    max_bytes = (width * height * 3) // 8
    if len(message_with_delimiter) > max_bytes:
        raise ValueError(
            f"Message too long! Maximum {max_bytes} characters, your message is {len(message_with_delimiter)} characters"
        )

    message_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel

        if message_index < len(binary_message):
            r = (r & 0xFE) | int(binary_message[message_index])
            message_index += 1

        if message_index < len(binary_message):
            g = (g & 0xFE) | int(binary_message[message_index])
            message_index += 1

        if message_index < len(binary_message):
            b = (b & 0xFE) | int(binary_message[message_index])
            message_index += 1

        new_pixels.append((r, g, b))

    stego_img = Image.new("RGB", (width, height))
    stego_img.putdata(new_pixels)

    if not output_path.lower().endswith(".png"):
        base_path = os.path.splitext(output_path)[0]
        output_path = base_path + ".png"
        print(f"[!] Output format enforced to PNG: {output_path}")

    stego_img.save(output_path, "PNG")

    print(f"\n[✓] Message successfully hidden in image!")
    print(f"[✓] Image saved to: {output_path}")


def extract_lsb(image_path: str) -> str:
    try:
        img = Image.open(image_path)
        print(f"[i] Image format: {img.format}")
    except Exception as e:
        raise ValueError(f"Failed to open image: {e}")

    if img.mode != "RGB":
        img = img.convert("RGB")

    pixels = list(img.getdata())
    binary_message = ""

    for pixel in pixels:
        r, g, b = pixel
        binary_message += str(r & 1)
        binary_message += str(g & 1)
        binary_message += str(b & 1)

    message = binary_to_string(binary_message)

    if "###END###" in message:
        message = message.split("###END###")[0]

    return message
