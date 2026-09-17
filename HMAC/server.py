import socket
import hmac
import hashlib 
import threading
def receive_messages(sock):
    key = b"hello world"
    while True:
        try:
            data = sock.recv(4096).decode()
            if not data:
                print("\n[-] Client disconnected.")
                break
            list1 = data.split(",")
            message = list1[0]
            hmac1 = list1[1]
            hmac2 = hmac.new(key,bytes(message,'utf-8'),hashlib.sha256).hexdigest()
            if hmac1 == hmac2 :
                print(f"\n[Client]: {message}\n[You]: ", end="")
            else : 
                print("[+] The message altered")
        except:
            break
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",5000))
s.listen(1)
c,a = s.accept()
key = b"hello world"
threading.Thread(target=receive_messages, args=(c,), daemon=True).start()
while True :
    message = input("[+] Enter message : ")
    hmac1 = hmac.new(key,bytes(message,'utf-8'),hashlib.sha256).hexdigest()
    msg = message+","+hmac1
    c.sendall(msg.encode())
    
c.close()
s.close()
