strings = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message = input("[+] Enter message: ").lower()
key = input("[+] Enter key: ").lower()
choose = input("[+] Do you want Encrypt (e) or Decrypt (d): ").strip().lower()
key_indices = [strings.index(c) for c in key if c in strings]
if not key_indices:
    print("[+] Key must include valid characters.")
    exit()
result = ""
key_idx = 0 
for char in message:
    if char in strings:
        x = strings.index(char)
        k = key_indices[key_idx % len(key_indices)] 
        if choose == "e":
            new_index = (x + k) % 26
        else:
            new_index = (x - k) % 26
        result += strings[new_index]
        key_idx += 1
    else:
        result += char  
if choose == "e":
    print("[+] Encrypted message:", result)
else:
    print("[+] Decrypted message:", result)
