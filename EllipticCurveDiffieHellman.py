from sys import exit
from sympy import isprime
import hashlib
from sage.all import * 
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import sys
def Generatekey(x) : 
    choose1 = input("[+] What algorithm hash do you want to decrypt : ")
    choose2 = input("[+] How long is the key ?(16,24,32): ")
    if choose1 == "md5" : 
        hash1 = hashlib.md5(str(x).encode()).digest()
    elif choose1 == "sha1" : 
        hash1 = hashlib.sha1(str(x).encode()).digest()
    elif choose1 == "sha256" : 
        hash1 = hashlib.sha256(str(x).encode()).digest()
    elif choose1 == "sha512" :
        hash1 = hashlib.sha512(str(x).encode()).digest()
    if choose2 == "16" : 
        d = hash1[0:16]
    elif choose2 == "24":
        d = hash1[0:24]
    elif choose2 == "32":
        d = hash1[0:32]
    return d
def converhextoint(n) : 
    if n.startswith("0x") : 
        x = n[2:]
        y = bytes.fromhex(x)
        z = int.from_bytes(y)
        return z
    return int(n)
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
def multiplyPoint(k, x, y, a, p):
    rx, ry = None, None
    qx, qy = x, y
    while k > 0:
        if k % 2 == 1:
            rx, ry = additionPoint(rx, ry, qx, qy, a, p)
        qx, qy = additionPoint(qx, qy, qx, qy, a, p)
        k //= 2
    return rx, ry
def tonelli_shanks(n, p):
    n %= p
    if n == 0:
        return 0
    if pow(n, (p - 1) // 2, p) != 1:
        return None
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        t2i, i = t, 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, (b * b) % p, (t * b * b) % p, (r * b) % p
    return r
p1 = input("[+] Enter GF (galois field): ")
p = converhextoint(p1)
if not isprime(p):
    print("[+] Not prime")
    exit()
if p <= 3:
    print("[+] p is so small")
    exit()
a2 = input("[+] Enter a : ")
a1 = converhextoint(a2)
b2 = input("[+] Enter b : ")
b1 = converhextoint(b2)
px = int(input("[+] Enter Px : ")) % p
py = int(input("[+] Enter Py : ")) % p
shared_x = 0
choose = input("[+] Enter do you have private key for both ?y/n : ")
if choose == "y":
    xa = int(input("[+] Enter key private for first person : "))
    xb = int(input("[+] Enter key private for second person : "))
    ax, ay = multiplyPoint(xa, px, py, a1, p)
    print(f"[+] Alice Public Key A = ({ax}, {ay})")
    bx, by = multiplyPoint(xb, px, py, a1, p)
    print(f"[+] Bob Public Key B = ({bx}, {by})")
    tab_alice_x, tab_alice_y = multiplyPoint(xa, bx, by, a1, p)
    tab_bob_x, tab_bob_y = multiplyPoint(xb, ax, ay, a1, p)
    if tab_alice_x == tab_bob_x and tab_alice_y == tab_bob_y:
        print(f"[+] The secret key ({tab_alice_x},{tab_alice_y})")
    else:
        print("[+] Shared secrets do not match — check inputs")
else:
    point1 = input("[+]Do you have for any one ? : ")
    if point1 == "y" :
        xa = int(input("[+] Enter key private for first person : "))
        choose1 = input("[+] Do you have point (x,y) : ")
        if choose1 == "y":
            bx = int(input("[+] Enter Public Key x : ")) % p
            by = int(input("[+] Enter Public Key y : ")) % p
        else:
            Aq = int(input("[+] Enter number It will be made up for elsewhere x in equation : ")) % p
            rhs = (pow(Aq, 3, p) + a1 * Aq + b1) % p
            yequation = tonelli_shanks(rhs, p)
            if yequation is None:
                print("[+] No valid point on the curve for this x")
                exit()
            print(f"[+] P({Aq}, {yequation}) or P({Aq}, {p - yequation})")
            bx = Aq
            by = yequation
        ax, ay = multiplyPoint(xa, px, py, a1, p)
        print(f"[+] Your Public Key A = ({ax}, {ay})")
        shared_x, shared_y = multiplyPoint(xa, bx, by, a1, p)
        print(f"[+] The secret key is ({shared_x}, {shared_y})")
        hash1 = hashlib.sha1(str(shared_x).encode()).hexdigest()
        print(f"[+] The secret key is {shared_x} sha1 : {hash1}")
    else : 
        point2 = input("[+] Do you have public point for both : ")
        if point2 == "y" : 
            E = EllipticCurve(GF(p), [a1, b1])
            Qax = int(input("[+] Enter x : "))
            Qay = int(input("[+] Enter y : "))
            Qbx = int(input("[+] Enter x : "))
            Qby = int(input("[+] Enter y : "))
            Q_A = E(Qax,Qay)
            Q_B = E(Qbx,Qby)
            G = E(px,py)
            nA = discrete_log(Q_A, G, operation='+')
            print("[+] The secret Key for first person is :",nA)
            nB = discrete_log(Q_B, G, operation='+')
            print("[+] The secret Key for second person is :",nB)
            shared1 = nA*Q_B
            shared2 = nB*Q_A
            print("[+] Check if shared key 1 equal 2")
            if shared1 == shared2 : 
                print("[+] True")
                shared_x = shared1[0]
                shared_y = shared1[1]
                print(f"[+] x : {shared_x} , y : {shared_y}")
                print(f"[+] The secret key is {shared_x} ")
            else : 
                print("[+] point not true")
        else : 
            point3 = input("[+] Do you have public point for one : ")
            if point3 == "y" :
                E = EllipticCurve(GF(p), [a1, b1])
                Qax = int(input("[+] Enter x : "))
                Qay = int(input("[+] Enter y : "))
                Q_B = E(Qax,Qay)
                G = E(px,py)
                nA = discrete_log(Q_A, G, operation='+')
                shared1 = nA*Q_B
                shared_x = shared1[0]
                shared_y = shared1[1]
                print(f"[+] x : {shared_x} , y : {shared_y}")
                print(f"[+] The secret key is {shared_x} ")
while True : 
    x = input("[+] Do you want decrypt ? y/n: ")
    if x == "y" :
        key = Generatekey(shared_x)
        iv2 = input("[+] Enter iv : ")
        iv = bytes.fromhex(iv2)
        cipher1 = input("[+] Enter ciphertext : ")
        cipher = bytes.fromhex(cipher1)
        decipher = AES.new(key,AES.MODE_CBC,iv)
        plaintext = unpad(decipher.decrypt(cipher),AES.block_size)
        print(plaintext)
        break
    else : 
        break
