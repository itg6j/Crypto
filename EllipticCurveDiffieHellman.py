from sys import exit
from sympy import isprime
import hashlib
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
p = int(input("[+] Enter GF (galois field): "))
if not isprime(p):
    print("[+] Not prime")
    exit()
if p <= 3:
    print("[+] p is so small")
    exit()
a1 = int(input("[+] Enter a : "))
b1 = int(input("[+] Enter b : "))
px = int(input("[+] Enter Px : ")) % p
py = int(input("[+] Enter Py : ")) % p
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
