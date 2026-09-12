from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
key = input("[+] Enter key size(16,24,32)byte: ")
flag = input("[+] Enter message or ciphertext : ")
if len(key) not in (16,24,32) : 
    print("[+] Error: Key length must be exactly 16, 24, or 32 bytes.")
    exit()
KEY = key.encode()
FLAG = flag
choose = input("[+] Do you want encrypt or decrypt (e/d): ")
if choose == "d" : 
    def decrypt(ciphertext):
        ciphertext = bytes.fromhex(ciphertext)
        cipher = AES.new(KEY, AES.MODE_ECB)
        try:
            decrypted_padded = cipher.decrypt(ciphertext)
            decrypted = unpad(decrypted_padded, AES.block_size)
            return("plaintext :", decrypted.decode())
        except ValueError as e:
            return {"error": str(e)}
    c_hex = decrypt(FLAG)
    print(c_hex)
else : 
    def encrypt_flag():
        cipher = AES.new(KEY, AES.MODE_ECB)
        padded_data = pad(FLAG.encode(), AES.block_size)
        encrypted = cipher.encrypt(padded_data)
        return("ciphertext :", encrypted.hex())
    c_hex = encrypt_flag()
    print(c_hex)
