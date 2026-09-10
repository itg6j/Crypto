from math import gcd
def modularBionmials(e1,e2,c1,c2,N,a1,a2) : 
    q = gcd(pow(a2,(-e2 * e1),N) * pow(c2, e1, N) - pow(a1, (-e1 * e2), N) * pow(c1, e2, N), N)
    p = N//q
    return p ,q 
n = int(input("[+] Enter modulus : "))
e1 = int(input("[+] Enter exponent first equation : "))
a1 = int(input("[+] Enter first number a : "))
c1 = int(input("[+] Enter ciphertext 1 : "))
e2 = int(input("[+] Enter exponent second equation : "))
a2 = int(input("[+] Enter second number a : "))
c2 = int(input("[+] Enter ciphertext 2 : "))
p ,q = modularBionmials(e1,e2,c1,c2,n,a1,a2)
print(f"[+] p = {p}")
print(f"[+] q = {q}")

