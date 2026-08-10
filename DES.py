from Crypto.Cipher import DES 
from Crypto.Util.Padding import pad,unpad
key = input("Enter key contain 8 character :") #8-bit
plaintext =input("Enter word you want encrypt : ")
cipher = DES.new(key.encode(),DES.MODE_ECB)
ciphertext = cipher.encrypt(pad(plaintext.encode(),DES.block_size))
print("ciphertext : ",ciphertext.hex())
decipher = DES.new(key.encode(),DES.MODE_ECB)
deciphertext = unpad(cipher.decrypt(ciphertext),DES.block_size)
print("plaintext : ",deciphertext.decode())