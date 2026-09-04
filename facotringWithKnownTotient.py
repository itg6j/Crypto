from math import isqrt 
n = int(input("[+] Enter n: "))
phi = int(input("[+] Enter phi: "))
s= n - phi + 1
delta = s**2 - 4 * n
sqrt_delta = isqrt(delta)
if sqrt_delta * sqrt_delta != delta:
    print("[+] wrong")
else:
    p = (s + sqrt_delta) // 2
    q = (s - sqrt_delta) // 2
    print(f"[+] p = {p}")
    print(f"[+] q = {q}")
    print(f"[+] check (p * q == n): {p * q == n}")
