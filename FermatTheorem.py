from math import gcd
from sympy import isprime
import sys
def fermat(number,exponent,prime) : 
    x = exponent % (prime-1)
    result  = pow(number,x,prime)
    return result
a = int(input("[+] Enter number : "))
e = int(input("[+] Enter exponention : "))
p = int(input("[+] Enter prime modulus : "))
x = isprime(p)
if x== False: 
    print("[+] modulus not prime")
    sys.exit
if gcd(a,p) == 1 : 
    y = fermat(4,532,11)
    print(f"[+] result : {y} mod {p}")
else : 
    print("[+] gcd != 1")
