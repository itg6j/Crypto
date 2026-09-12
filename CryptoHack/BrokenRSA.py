from sympy import isprime
def legendre_symbol(a: int, p: int) -> int:
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls
def modular_sqrt(n, p):
    n %= p
    if n == 0:
        return (0, 0)
    if p == 2:
        return (n, n)
    if legendre_symbol(n, p) != 1:
        return None
    if p % 4 == 3:
        r = pow(n, (p + 1) // 4, p)
        return (r, p - r)
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    while t != 1:
        t2i, i = t, 0
        for i in range(1, m):
            t2i = pow(t2i, 2, p)
            if t2i == 1:
                break
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    return r
n = int(input("[+] Enter number : "))
p = int(input("[+] Enter modulus prime : "))
if isprime(p) == False : 
    print("[+] modulus is not prime")
roots = modular_sqrt(n, p)
c = int(input("[+] Enter ciphertext : "))
curr = [c]
for _ in range(4):
    next_curr = []
    for val in curr:
        res = modular_sqrt(val, p)
        if res is not None:
            if isinstance(res, tuple):
                next_curr.extend(res)
            else:
                next_curr.append(res)
                next_curr.append((p - res) % p)
    curr = list(set(next_curr))
for m in curr:
    try:
        hex_str = hex(m)[2:]
        if len(hex_str) % 2 != 0: hex_str = '0' + hex_str
        b = bytes.fromhex(hex_str)
        if b'flag' in b:
            print(f"\n [+] Flag: {b.decode('utf-8', errors='ignore')}")
    except:
        pass
