from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
key = input("[+] Enter key (must be 16, 24, or 32 characters): ").encode()
flag = input("[+] Enter message : ").encode()
if len(key) not in (16,24,32) : 
    print("[+] Error: Key length must be exactly 16, 24, or 32 bytes.")
    exit()
choose = input("[+] Do you want encrypt or decrypt (e/d): ")
if choose == "e" : 
    iv = os.urandom(16)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    ciphertext = cipher.encrypt(pad(flag,AES.block_size))
    civ = iv+ciphertext
    print("[+] ciphertext :",civ.hex())
else :
    raw = bytes.fromhex(flag.decode())
    x = input("[+] Do you know iv  y/n (hex): ")
    if x =="y" : 
        y = input("[+] Enter you iv : ")
        riv = bytes.fromhex(y)
    else :
        riv = raw[:16]
    ciphertext = raw[16:]
    decipher = AES.new(key,AES.MODE_CBC,riv)
    deciphertext = unpad(decipher.decrypt(ciphertext),AES.block_size)
    print("[+]Message :",deciphertext.decode())
