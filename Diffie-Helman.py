from sympy import isprime
import sys
q = int(input("[+] Enter Prime modulus : "))
x = isprime(q)
if x == False : 
    sys.exit()
alpha = int(input("[+] Enter primitive root or alpha : "))
Xa = int(input("[+] Enter private key for first person : "))
Xb = int(input("[+] Enter private key for second person : "))
b = pow(alpha,Xa,q)
a = pow(alpha,Xb,q)
k1 = pow(b,Xb,q)
k2 = pow(a,Xa,q)
status = None
if k1 == k2 : 
    status = True
    print(f"[+] if key first person equal key second person :  {status}  , key is : {k1}")
