from math import gcd
n = int(input("[+] Enter n : "))
a = int(input("[+] Enter a : "))
b = int(input("[+] Enter b : "))
d = 0
for i in range(n) : 
    a = ((a**2)+1) %n
    b = ((b**2)+1) %n
    b = ((b**2)+1) %n
    d = gcd((a-b),n)
    if 1<d and d<n and d != 1 : 
        print("p = : ",d)
        q = n//d
        print("q = : ",q)
        n1 = d * q
        if n == n1 : 
            print(f"[+] {n1} = {d} x {q}: ",True)
        break 
