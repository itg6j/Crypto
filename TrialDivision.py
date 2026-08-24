from math import isqrt
from sympy import isprime
n = int(input("[+] Enter modulus : "))
x = isqrt(n)
p=x
q=x
while True:
    if n % p == 0 and isprime(p) == True:
        break
    p=p+1
while True:
    if n % q == 0 and isprime(q) == True:
        break
    q=q-1
print(f"[+] The factor is : {p} , {q}")
