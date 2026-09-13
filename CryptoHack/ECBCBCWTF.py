import requests
x = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/")
ciohertext1=x.json()['ciphertext']
print(len(ciohertext1))
print(ciohertext1)
ciphertext = bytes.fromhex(ciohertext1)
iv= ciphertext[:16].hex()
x = ciphertext[16:].hex()
print(iv)
print(x)
list1 = []
for i in range(0,len(x),32):
    list1.append(x[i:i+32])
list2 = []
for i in list1 : 
    y = requests.get(f"https://aes.cryptohack.org/ecbcbcwtf/decrypt/{i}/")
    list2.append(y.json()['plaintext'])
decrypted_bytes = bytes.fromhex(list2[0])
iv_bytes = bytes.fromhex(iv)
c1 = bytes(a ^ b for a, b in zip(decrypted_bytes, iv_bytes))
decrypt = bytes.fromhex(list2[1])
decrypted_bytes2 = bytes.fromhex(list2[1])
previous_ciphertext = bytes.fromhex(list1[0]) # البلوك المشفر الأول
c2 = bytes(a ^ b for a, b in zip(decrypted_bytes2, previous_ciphertext))
print(f"{c1.decode('ascii')}{c2.decode('ascii')}")
