import requests
import hashlib
import binascii
from Crypto.Cipher import AES
x = requests.get("https://aes.cryptohack.org/passwords_as_keys/encrypt_flag")
ciohertext=x.json()['ciphertext']
print(ciohertext)
with open('words.txt','r')as f:
    for word in f:
        word1 = word.split()[0]
        key = hashlib.md5(word1.encode()).digest()
        cipher = AES.new(key,AES.MODE_ECB)
        ciphertext = bytes.fromhex(ciohertext)
        decrypyed = cipher.decrypt(ciphertext)
        result = binascii.unhexlify(decrypyed.hex())
        print(result)
        if result.startswith('crypto{'.encode()):
            print("key is %s" % word)
            print(result.decode('utf-8'))
            exit()
