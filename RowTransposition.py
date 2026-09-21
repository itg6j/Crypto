choice = input("[+] Choose (e)ncrypt or (d)ecrypt : ").strip().lower()
key = input("[+] Enter key (e.g. 4312) : ")
lenkey = len(key)
key_order = sorted([(digit, idx) for idx, digit in enumerate(key)])

if choice == "e":
    message = input("[+] Enter message : ")
    m = "".join(message.split())    
    remainder = len(m) % lenkey
    if remainder != 0:
        m += "x" * (lenkey - remainder)
    list1 = [m[i:i+lenkey] for i in range(0, len(m), lenkey)]
    cipher = ""
    for digit, col_idx in key_order:
        for row in list1:
            cipher += row[col_idx]
    print("[+] Encrypted message :", cipher)
elif choice == "d":
    cipher = input("[+] Enter cipher message : ")
    num_rows = len(cipher) // lenkey
    columns = [""] * lenkey
    curr = 0
    for digit, col_idx in key_order:
        columns[col_idx] = cipher[curr : curr + num_rows]
        curr += num_rows
    plain = ""
    for r in range(num_rows):
        for c in range(lenkey):
            plain += columns[c][r]
    print("[+] Decrypted message :", plain)
