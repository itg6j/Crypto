import galois
from sys import exit
from sympy import isprime
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
    rx, ry = x, y
    for _ in range(k - 1):
        rx, ry = additionPoint(rx, ry, x, y, a, p)
    return rx, ry
p = int(input("[+] Enter GF (galois field): "))
if not isprime(p): 
    print("[+] Not prime")
    exit()
if p <= 3: 
    print("[+] p is so small")
    exit()
GF = galois.GF(p)
a1 = int(input("[+] Enter a : "))
b1 = int(input("[+] Enter b : "))
px = int(input("[+] Enter Px : "))
py = int(input("[+] Enter Py : "))
xa = int(input("[+] Enter key private for first person : "))
xb = int(input("[+] Enter key private for second person : "))
ax, ay = multiplyPoint(xa, px, py, a1, p)
print(f"[+] Alice Public Key A = ({ax}, {ay})")
bx, by = multiplyPoint(xb, px, py, a1, p)
print(f"[+] Bob Public Key B = ({bx}, {by})")
tab_alice_x, tab_alice_y = multiplyPoint(xa, bx, by, a1, p)
tab_bob_x, tab_bob_y = multiplyPoint(xb, ax, ay, a1, p)
if tab_alice_x == tab_bob_x and tab_alice_y == tab_bob_y : 
    print(f"[+] The secret key ({tab_alice_x},{tab_alice_y})")
