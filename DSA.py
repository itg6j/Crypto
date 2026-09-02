from Crypto.Util.number import isPrime
def GenerateKey():
    p = int(input("[+] Enter p : "))
    q = int(input("[+] Enter q : "))
    if isPrime(p) == False : 
        print("[+] p is not prime")
    if isPrime(q) == False : 
        print("[+] q is not prime")
    g = int(input("[+] Enter generator : "))
    x = int(input("[+] Enter private key : "))
    if not(1<= x <= q-1) :
        print(f"[+] private key wrong must be 1<= x <= {q-1}")
    ca = (p-1)//q
    a = pow(g,ca,p)
    if a == 1 : 
        print("[+] generator can't cyclic group")
    y = pow(g,x,p)
    print(f"\n[+] public key is p = {p}\n[+] q = {q}\n[+] g = {g}\n[+] y = {y}\n")
    return p,q,g,y
def Signature(p,q,g) : 
    k = int(input("[+] Enter message int : "))
    x = int(input("[+] Enter private key : "))
    h = int(input("[+] Enter value hash message int : "))
    if not(0<k<q) : 
        print("[+] wronge message long")
    r = pow(g,k,p)%q
    kinv = pow(k,-1,q)
    s = kinv*(h+r*x)%q
    print(f"[+] The signature for m is the pair s = {s}\n[+] r = {r}\n")
    return r,s,h
def verifiction(r,s,g,p,q,h,y) : 
    if not(0<r<q)  : 
        print(f"[+] r not in range 0<{r}<{q}")
    if not(0<s<q)  : 
            print(f"[+] s not in range 0<{s}<{q}")
    w = pow(s,-1,q)
    u1 = w*h%q
    u2 = r*w%q
    v = ((g**u1)*(y**u2)%p)%q
    if v == r : 
        print("[+] accept the signature")
choose = input("[+] do you want generate key and singnature and verification ?? y/n : ")
if choose == "y" : 
    p,q,g,y = GenerateKey()
    r,s,h =Signature(p,q,g) 
    verifiction(r,s,g,p,q,h,y)
else : 
    choose1 = input("[+] what you want keyGeneration or Signature or verification?? k/s/v  : ")
    if choose1 == "k" : 
        GenerateKey() 
    elif choose1 == "s" : 
        p = int(input("[+] Enter p : "))
        q = int(input("[+] Enter q : "))
        g = int(input("[+] Enter g : "))
        Signature(p,q,g) 
    else : 
        r = int(input("[+] Enter r : "))
        s = int(input("[+] Enter s : "))
        p = int(input("[+] Enter p : "))
        q = int(input("[+] Enter q : "))
        g = int(input("[+] Enter g : "))
        h = int(input("[+] Enter h : "))
        y = int(input("[+] Enter y : "))
        verifiction(r,s,g,p,q,h,y)