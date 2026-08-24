from math import gcd
def extendEuclidean(a, b): 
    s1, s2 = 1, 0
    t1, t2 = 0, 1    
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        s = s1 - q * s2
        t = t1 - q * t2
        s1, s2 = s2, s
        t1, t2 = t2, t
    return s1, t1
num1 = int(input("[+] Enter a : "))
num2 = int(input("[+] Enter b : "))
x, y = extendEuclidean(num1, num2) 
gcd1 = gcd(num1,num2)
print("[+] GCD =", gcd1)
print("[+] x =", x)
print("[+] y =", y)
z = (x*num1)+(y*num2)
status = None
if gcd1 == z : 
    status = True
print(f"[+] if s * a + t * b = gcd(a,b) ??? result = {z}, gcd = result : {status}")
