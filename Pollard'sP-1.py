from math import gcd, factorial
import sys
n = int(input("[+] Enter modulus : "))
a = 2
if gcd(n,a) != 1 : 
    for i in range(3,n) : 
        if gcd(n,i) == 1 : 
            a = i
            break
if gcd(n,a) == 1 : 
    k1 = 1
    while True : 
        k = factorial(k1)#1!
        e = pow(a,k,n)
        h= e % n
        p = gcd(h-1,n)
        q = n//p
        if p == 1 : 
            k1 = k1+1 
        elif p == n:
            print("[+] Failed with this base a, try another one")
            sys.exit()
        else : 
            break
    print(f"[+] factor p is :  {p} q : {q}")
