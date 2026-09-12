import socket
import os
import hashlib
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
p =32317006071311007300338913926423828248817941241140239112842009751400741706634354222619689417363569347117901737909704191754605873209195028853758986185622153212175412514901774520270235796078236248884246189477587641105928646099411723245426622522193230540919037680524235519125679715870117001058055877651038861847280257976054903569732561526167081339361799541336476559160368317896729073178384589680639671900977202194168647225871031411336429319536193471636533209717077448227988588565369208645296636077250268955505928362751121174096972998068410554359584866583291642136218231078990999448652468262416972035911852507045361090559
g = 2
def receive_messages(sock, aes_key):
    while True:
        try:
            payload = sock.recv(4096)
            if not payload:
                print("\n[+] Client disconnected.")
                os._exit(0)            
            iv = payload[:16]
            ciphertext = payload[16:]
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
            print(f"\n[Client]: {decrypted.decode()}")
            print("[Server (You)]: ", end="", flush=True)
        except Exception:
            break
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 65432))
    server.listen(1)
    print("[+] Server listening on 127.0.0.1:65432...")
    conn, addr = server.accept()
    print(f"[+] Connected to Client at {addr}")
    server_private = int.from_bytes(os.urandom(32), 'big')
    server_public = pow(g, server_private, p)
    conn.sendall(str(server_public).encode())
    client_public = int(conn.recv(4096).decode())
    shared_secret = pow(client_public, server_private, p)
    shared_bytes = shared_secret.to_bytes((shared_secret.bit_length() + 7) // 8, 'big')
    aes_key = hashlib.sha256(shared_bytes).digest()
    threading.Thread(target=receive_messages, args=(conn, aes_key), daemon=True).start()
    while True:
        try:
            msg = input("[+]Server: ")
            if not msg.strip():
                continue
            iv = os.urandom(16)
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(msg.encode(), AES.block_size))
            conn.sendall(iv + ciphertext)
        except (KeyboardInterrupt, EOFError):
            print("\n[+] Exiting")
            break
    conn.close()
    server.close()

main()
