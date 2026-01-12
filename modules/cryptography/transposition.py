def transposEncrypt(plaintext: str, key: int):
    encrypt = ""
    columns = [""] * key
    plaintext_clean = plaintext.replace(" ", "").upper()

    for index, char in enumerate(plaintext_clean):
        column = index % key
        columns[column] += char

    max_len = max(len(col) for col in columns)

    for i in range(key):
        if len(columns[i]) < max_len:
            padding_count = max_len - len(columns[i])
            columns[i] += "Ø" * padding_count

    encrypt = "".join(columns)

    return encrypt


def transposDecrypt(ciphertext: str, key: int):
    decrypt = ""
    total_chars = len(ciphertext)
    num_rows = total_chars // key

    columns = []
    for i in range(key):
        start = i * num_rows
        end = start + num_rows
        col = ciphertext[start:end]
        columns.append(col)

    for i in range(num_rows):
        for j, col in enumerate(columns):
            if i < len(col):
                decrypt += col[i]

    decrypt = decrypt.replace("Ø", "")

    return decrypt
