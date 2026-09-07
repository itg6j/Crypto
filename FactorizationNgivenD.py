import random
import math
n = int(input("[+] Enter modulus : "))
e = int(input("[+] Enter public key : "))
d = int(input("[+] Enter private key : "))
k = (e*d)-1
while True : 
    g = random.randint(2,n-1)
    common = math.gcd(g, n)
    if 1 < common < n:
        p = common
        q = n // p
        print(f"[+] p = {p} q ={q}")
        break
    t = k//2
    while t % 2 == 0:
            t //= 2
            x = pow(g, t, n)
            if x > 1:
                y = math.gcd(x - 1, n)
                if 1 < y < n:
                    p = y
                    q = n // p
                    print(f"[+] p = {p} q ={q}")
                    break
    break
