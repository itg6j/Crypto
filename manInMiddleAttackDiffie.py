from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
p_str = input("[+] Enter modulus : ")
p = int(p_str,16)
g_str = input("[+] Enter generator : ")
g = int(g_str,16)
a = int(input("[+] Enter your private key : "))
A = pow(g,a,p)
A = hex(A)
print("JSON\n")
print("{\"p\":",f"\"{p_str}\"",", \"g\":",f"\"{g_str}\"",", \"A\":",f"\"{A}\"","}")
b = int(input("[+] Enter your private key : "))
B = pow(g,b,p)
B = hex(B)
B1 = int(B,16)
A1 = int(A,16)
print("{\"B\":",f"\"{B}\"","}")
secretA = pow(B1,a,p)
secretB = pow(A1,b,p)
if secretA == secretB: 
    print(f"[+] The Secret key is : {secretA}")
    iv1 = input("[+] Enter iv : ")
    iv=bytes.fromhex(iv1)
    c = input("[+] Enter ciphertext : ")
    ciphertext = bytes.fromhex(c)
    key = hashlib.sha1(str(secretA).encode()).digest()[:16]
    key = hashlib.sha1(str(secretA).encode()).digest()[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = unpad(cipher.decrypt(ciphertext), 16)

    print("FLAG:", flag.decode())
else : 
    print("[+] wrong")
