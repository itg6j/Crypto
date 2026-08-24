import sys
from math import gcd
def extendEuclidean(a, b): 
    t1, t2 = 0, 1    
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        t = t1 - q * t2
        t1, t2 = t2, t
    return  t1
num1 = int(input("[+] Enter big number : "))
num2 = int(input("[+] Enter small number : "))
x = extendEuclidean(num1,num2) 
gcd1 = gcd(num1,num2)
if gcd1 != 1 : 
    print("[+] The gcd not equal 1 ")
    sys.exit()
print("[+] GCD =", gcd1)
y = x%num1
print("[+] The inverse is =", y)
z = num1*y 
