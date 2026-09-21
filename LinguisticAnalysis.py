from collections import Counter
import string
def crack_caesar_by_frequency(ciphertext):
    letters_only = [c.upper() for c in ciphertext if c.isalpha()]
    if not letters_only:
        return "no letters"
    counts = Counter(letters_only)
    most_common_char, freq = counts.most_common(1)[0]
    c_val = ord(most_common_char) - ord('A')
    e_val = ord('E') - ord('A')  
    key = (c_val - e_val) % 26    
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)            
    return key, most_common_char, "".join(decrypted)
cipher = input("[+] Enter ciphertext : ")
key, common_char, plain = crack_caesar_by_frequency(cipher)
print(f"(Key): {key}")
print(f"message is : {plain}")
