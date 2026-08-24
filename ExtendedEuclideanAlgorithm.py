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
    return a, s1, t1
num1 = int(input("[+] Enter e : "))
num2 = int(input("[+] Enter phi : "))
gcd, x, y = extendEuclidean(num1, num2) 
print("[+] GCD =", gcd)
print("[+] x =", x)
print("[+] y =", y)
z = (x*num1)+(y*num2)
status = None
if x == 1 : 
    status = True
else : 
    status = False
print(f"[+] if s * a + t * b = gcd(a,b) ??? The status is : {status} , result = {z}")
