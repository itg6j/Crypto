import socket 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import threading 
import os
import hashlib
import json
def point_mult(k, Px, Py, a, p):
    rx, ry = None, None
    qx, qy = Px, Py
    while k > 0:
        if k & 1:
            rx, ry = additionPoint(rx, ry, qx, qy, a, p)
        qx, qy = additionPoint(qx, qy, qx, qy, a, p)
        k >>= 1
    return rx, ry
def recvmessage(c,aeskey) : 
    while True : 
        try :
            payload = c.recv(4096)
            if not payload : 
                print("[+] Client Disconnected")
                exit(1)
            ciphertext = bytes.fromhex(payload.decode())
            iv = ciphertext[:16]
            ciphertext1 = ciphertext[16:]
            decyper = AES.new(aeskey,AES.MODE_CBC,iv)
            decrypted = unpad(decyper.decrypt(ciphertext1),AES.block_size)
            print(f"\n[+] Client: {decrypted.decode()}")
            print("[+] Server: ", end="", flush=True)
        except : 
            print("[+] Exting")
def additionPoint(x1, y1, x2, y2, a, p):
    if x1 is None: return x2, y2
    if x2 is None: return x1, y1
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return None, None
    if x1 == x2 and y1 == y2:
        num = (3 * (x1**2) + a) % p
        den = (2 * y1) % p
        s = (num * pow(den, -1, p)) % p
    else:
        num = (y2 - y1) % p
        den = (x2 - x1) % p
        s = (num * pow(den, -1, p)) % p
    x3 = (s**2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3
def AESencrypt(m,key) : 
    iv = os.urandom(16)
    cipher = AES.new(key,AES.MODE_CBC,iv)
    ciphertext = cipher.encrypt(pad(m.encode(),AES.block_size))
    c1 = (iv + ciphertext).hex().encode()
    return c1
def AESdecrypt(m,key) : 
    message = bytes.fromhex(m)
    iv = message[:16]
    ciph = message[16:]
    cipher = AES.new(key,AES.MODE_CBC,iv)
    ciphertext = unpad(cipher.decrypt(ciph),AES.block_size).decode()
    return ciphertext
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",5000))
p = 9739
n = 1001
Gx = 1804
Gy = 5368
a1 = 497
b = 1768
x,y = point_mult(n, Gx, Gy, a1, p)
client_data = json.loads(c.recv(4096).decode())
client_x = client_data["x"]
client_y = client_data["y"]
c.sendall(json.dumps({"x": x, "y": y}).encode())
shared_x, shared_y = point_mult(n, client_x, client_y, a1, p)
key = hashlib.sha256(str(shared_x).encode()).digest()[:16]
threading.Thread(target=recvmessage, args=(c, key), daemon=True).start()
while True : 
    message = input("[+] Enter message : ")
    ciphertext = AESencrypt(message,key)
    c.sendall(ciphertext)
c.close()
