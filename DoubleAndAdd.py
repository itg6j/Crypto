from Crypto.Util.number import isPrime
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
def point_mult(k, Px, Py, a, p):
    rx, ry = None, None
    qx, qy = Px, Py
    while k > 0:
        if k & 1:
            rx, ry = additionPoint(rx, ry, qx, qy, a, p)
        qx, qy = additionPoint(qx, qy, qx, qy, a, p)
        k >>= 1
    return rx, ry
p = int(input("[+] Enter number  modulus or GF: "))
if isPrime(p) == False : 
    print("[+] Not prime")
a1 = int(input("[+] Enter a : "))
b = int(input("[+] Enter b : "))
Gx = int(input("[+] Enter Generate point x : "))
Gy = int(input("[+] Enter Generate point y : "))
n = int(input("[+] Enter private key : "))
x,y = point_mult(n, Gx, Gy, a1, p)
print(f"[+] x = {x} , y = {y}")
