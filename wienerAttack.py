import math
e = int(input("[+] Enter Exponent public key : "))
n = int(input("[+] Enter modulus : "))
c = int(input("[+] Enter ciphertext : "))
qs = []
a = e
b = n
while True:
    q = a // b
    r = a % b
    qs.append(q)
    a = b
    b = r
    if r == 0:
        break
print("[+] Continued Fraction:", qs)
k_list = []  
d_list = []  
h0, h1 = 0, 1
k0, k1 = 1, 0
for q in qs:
    h_next = q * h1 + h0
    k_next = q * k1 + k0
    k_list.append(h_next)
    d_list.append(k_next)
    h0 = h1
    h1 = h_next
    k0 = k1
    k1 = k_next
print(k_list)
print(d_list)
for k, d in zip(k_list, d_list):
        if k == 0:
            continue
        if (e * d - 1) % k != 0:
            continue
        phi = (e * d - 1) // k
        print(k)
        print(d)
        print(phi)
        s = n - phi + 1
        delta = s * s - 4 * n
        if delta >= 0:
            root = math.isqrt(delta)
            if root * root == delta: 
                p = (s + root) // 2
                q = (s - root) // 2
                m = pow(c, d, n)
                print(f"[+] message = {m}")
                length = (m.bit_length() + 7) // 8
                flag_pure = m.to_bytes(length, 'big')
                print(flag_pure.decode())
                break
