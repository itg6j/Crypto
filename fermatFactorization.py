from math import isqrt
n = int(input("[+] Enter modulus : "))
if n%2 == 0 : 
    print("[+] number is even")
    exit()
rootN = isqrt(n)
a = rootN
if a*a < n : 
    a = a+1
while True : 
    result = (a**2)-n
    b = isqrt(result)
    if b*b == result : 
        if n == (a**2)-(b**2) : 
            p = a+b
            q = a-b
            print(f"[+] factor is a ={a} q ={b}")
            print(f"[+] factor is p = {p} q = {q}") 
            break
    a = a + 1
