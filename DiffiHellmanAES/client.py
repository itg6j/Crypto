import socket
import os 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import hashlib
import threading
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

q = 32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
g = 2
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(("127.0.0.1",5000))
print("[+] connect successfully")
privatekey = int.from_bytes(os.urandom(32))
publickey= pow(g,privatekey,q)
c.sendall(str(publickey).encode())
publiclient = c.recv(4096).decode()
secretkey = pow(int(publiclient),privatekey,q)
shared_bytes = secretkey.to_bytes((secretkey.bit_length() + 7) // 8, 'big')
aeskey = hashlib.sha256(shared_bytes).digest()
threading.Thread(target=recvmessage, args=(c, aeskey), daemon=True).start()
while True : 
    try: 
        message = input("[+] Enter message : ")
        iv = os.urandom(16)
        cipher = AES.new(aeskey,AES.MODE_CBC,iv)
        ciphertext = cipher.encrypt(pad(message.encode(),AES.block_size))
        c1 = (iv + ciphertext).hex().encode()
        c.sendall(c1)
    except : 
        print("[+] Exiting")
        break
c.close()
