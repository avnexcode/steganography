def transposEncrypt(plaintext: str, key: int, show_process: bool = False):
    encrypt = ""
    columns = [""] * key
    plaintext_clean = plaintext.replace(" ", "").upper()
    process = []

    if show_process:
        process.append(f"Plaintext (tanpa spasi): {plaintext_clean}")
        process.append(f"Jumlah kolom: {key}")
        process.append("\nMengisi kolom:")

    for index, char in enumerate(plaintext_clean):
        column = index % key
        columns[column] += char
        if show_process:
            process.append(f"  Karakter '{char}' (index {index}) → Kolom {column}")

    max_len = max(len(col) for col in columns)

    if show_process:
        process.append(f"\nPanjang kolom terpanjang: {max_len}")
        process.append("Menambahkan padding 'Ø':")

    for i in range(key):
        if len(columns[i]) < max_len:
            padding_count = max_len - len(columns[i])
            columns[i] += "Ø" * padding_count
            if show_process:
                process.append(f"  Kolom {i}: ditambah {padding_count} padding")

    if show_process:
        process.append("\nIsi kolom setelah padding:")
        for i, col in enumerate(columns):
            process.append(f"  Kolom {i}: {col}")

    encrypt = "".join(columns)

    if show_process:
        process.append(f"\nCiphertext: {encrypt}")

    return encrypt, process if show_process else encrypt


def transposDecrypt(ciphertext: str, key: int, show_process: bool = False):
    decrypt = ""
    total_chars = len(ciphertext)
    num_rows = total_chars // key
    process = []

    if show_process:
        process.append(f"Ciphertext: {ciphertext}")
        process.append(f"Panjang ciphertext: {total_chars}")
        process.append(f"Jumlah kolom: {key}")
        process.append(f"Panjang per kolom: {num_rows}")
        process.append("\nMemisahkan menjadi kolom:")

    columns = []
    for i in range(key):
        start = i * num_rows
        end = start + num_rows
        col = ciphertext[start:end]
        columns.append(col)
        if show_process:
            process.append(f"  Kolom {i}: {col}")

    if show_process:
        process.append("\nMembaca per baris:")

    for i in range(num_rows):
        for j, col in enumerate(columns):
            if i < len(col):
                decrypt += col[i]
                if show_process and i < 3:  # Hanya tampilkan 3 baris pertama
                    process.append(f"  Baris {i}, Kolom {j}: {col[i]}")

    decrypt = decrypt.replace("Ø", "")

    if show_process:
        process.append(f"\nPlaintext (setelah menghapus padding): {decrypt}")

    return decrypt, process if show_process else decrypt
