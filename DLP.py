from sympy import isprime
import sys
q = int(input("[+] Enter prime modulus : "))
x = isprime(q)
if x == False : 
    print("[+] not prime modulus")
    sys.exit()
g = int(input("[+] Enter generator : "))
for i in range(q) : 
    x = g*i%q
    if x == 1 : 
        print(f"[+] The inverse = {i}")
     
