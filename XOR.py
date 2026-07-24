from pwn import * 
data1 = b"crypto{new_string}"
key = b"label"
encryption = xor(data1,key)
print(encryption)
decryption = xor(encryption,key)
print(decryption)