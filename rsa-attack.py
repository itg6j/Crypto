from Crypto.Util.number import GCD,long_to_bytes,isPrime
from factordb.factordb import FactorDB
from colorama import Style,Fore
import gmpy2
from math import isqrt
import sys 
import time
##FF : Fully Factored (the number is completely factored into primes)
##CF : Composite with some factors known (incompletely factored)
##C : Composite , but no factpr are know yet
##p : Defintiely prime : P 
##PRP : Probably prime
##U : Unknown Status 
##Unit : The number is unit(specifically for the number 1 )
# n is p^2 
def Nprime(c,e,n) : 
    phi = n-1
    d = pow(e,-1,phi)
    m = pow(c,d,n)
    print(m)
    x = long_to_bytes(m)
    print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+x.decode('utf-8', errors='ignore'))
#Baby RSA 
def smallExpnentAttack(c,e):
    m,exact = gmpy2.iroot(c,e)
    if exact == True : 
        x = long_to_bytes(int(m))
        print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+x.decode('utf-8', errors='ignore'))
def normalRsa(n,c,e,f):
    print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"status : ",f.get_status())
    print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"factor : ", f.get_factor_list())
    factor = f.get_factor_list()
    try : 
        p = factor[0]
        q = factor[1]
        phi = (p-1)*(q-1)
        if GCD(phi,e) == 1: 
            print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"found inverse")
        d = pow(e,-1,phi)
        print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"d (inverse key) = ",d)
        m = pow(c,d,n)
        print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"message : ",m)
        try:
            flag = long_to_bytes(m)
            print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"Decrypted Message/Flag : ", flag.decode('utf-8', errors='ignore'))
        except Exception as err:
            print(Fore.RED+Style.BRIGHT+"[+]"+Style.RESET_ALL+"Could not convert to bytes:", err)
    except Exception : 
        print(Fore.RED+Style.BRIGHT+"[-]"+Style.RESET_ALL+"Error") 
def trialDivision(n) : 

    x = isqrt(n)
    p=x
    q=x
    while True:
        if n % p == 0 and isPrime(p) == True:
            break
        p=p+1
    while True:
        if n % q == 0 and isPrime(q) == True :
            break
        q=q-1
    if not (p*q == n) : 
        q = n//p 
    return p,q
def Pollard(n):
    strtime = time.time()
    timeout = 60
    B=100000
    if n % 2 == 0:
        return 2, n // 2        
    a = 2
    for k in range(2, B):
        if time.time() - strtime > timeout : 
            return None, None
        a = pow(a, k, n)
        p = GCD(a - 1, n)
        if 1 < p < n:
            return p, n // p
        elif p == n:
            break
    return None, None
def PollardRho(n) : 
    strtime = time.time()
    timeout = 60
    d = 0
    a = 2
    b = 2
    while True: 
        if time.time() - strtime>timeout :
            print(f"[+] Time out = {timeout} PollardRho")
            return None,None
        a = ((a**2)+1) %n
        b = ((b**2)+1) %n
        b = ((b**2)+1) %n
        d = GCD((a-b),n)
        if 1< d <n : 
            print("p = : ",d)
            q = n//d
            print("q = : ",q)
            n1 = d * q
            if n == n1 : 
                print(f"[+] {n1} = {d} x {q}: ",True)
            break 
    return p,q
def fermatFactorization(n) : 
    strtime = time.time()
    timeout = 60
    if n%2 == 0 : 
        print("[+] number is even")
        exit()
    rootN = isqrt(n)
    a = rootN
    if a*a < n : 
        a = a+1
    while True : 
        if time.time() - strtime>timeout :
            print(f"[+] Time out = {timeout} Fermat Factorization")
            return None,None
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
    return p,q
def factor(n) : 
    f = FactorDB(n)
    f.connect()
    x = f.get_status()
    y = f.get_factor_list()
    return x,y
def bruteforce(n) : 
    if len(str(n))<= 8 :
        p,q = trialDivision(n)
    elif len(str(n))<= 12 :
        p,q = PollardRho(n)
    else : 
        p,q = Pollard(n)
        p,q = fermatFactorization(n)
    print(f"[+] factor is p = {p} q = {q}")
    return p,q
def factoringWithKnownTotient(n,phi) : 
    s= n - phi + 1
    delta = s**2 - 4 * n
    sqrt_delta = isqrt(delta)
    if sqrt_delta * sqrt_delta != delta:
        print("[+] wrong")
    else:
        p = (s + sqrt_delta) // 2
        q = (s - sqrt_delta) // 2
        print(f"[+] p = {p}")
        print(f"[+] q = {q}")
        print(f"[+] check (p * q == n): {p * q == n}")
        return p,q
def CRTRSA(c,dp,dq,p,q) : 
    qInv = pow(q,-1,p) 
    m1 = pow(c , dp, p)
    m2 = pow(c , dq, q)
    h = (qInv * (m1 - m2)) % p
    m = m2 + (h * q)
    print(f"[+] message : {m}")
choose =input("[+] Do you want factor n or you have c,e,n and do you want attack f/a ?? :")
if choose == "f" : 
    n = int(input("[+] Enter modulus : "))
    status , factor1 = factor(n) 
    if status == "FF" :
        print("[+] factor :",factor1)
        if 3>=len(factor1) :  
            bruteforce(n)
    elif status =="C" :
        choose1 = input("[+] you know phi or Totient y/n : ") 
        phi = int(input("[+] Enter phi : "))
        if choose1 == "y" : 
            factoringWithKnownTotient(n,phi)
        else : 
            bruteforce(n)
elif choose == "a" : 
    print("="*45)
    print("\n[+] RSA-CRT Decryption (Fast using: p, q, dp, dq, c) ")
    print("[+] Standard RSA Attack (Given: n, e, c)\n")
    choose1 = input("Enter number  (1,2,...): ")
    if choose1 == "2" : 
        n = int(input("[+] Enter modulus : "))
        c = int(input("[+] Enter ciphertext : "))
        e = int(input("[+] Enter public key : "))
        x,y = factor(n)
        if x =="P" : 
            Nprime(c,e,n)
        elif x == "FF": 
            if len(y) >= 2 and y[0] == y[1] : 
                    p = isqrt(n)
                    phi = p * (p-1)
                    d = pow(e, -1, phi)
                    m = pow(c, d, n)
                    print(Fore.CYAN+Style.BRIGHT+"[+]"+Style.RESET_ALL+"Flag String:", long_to_bytes(m).decode("utf-8", errors="ignore"))
                    sys.exit()
            if n>c  : 
                normalRsa(n,c,e,y)
        elif n>c: 
            smallExpnentAttack(c,e)
        elif x =="C" : 
            p,q = bruteforce(n)
        else: 
            print(Style.BRIGHT+Fore.RED+"[-]"+Style.RESET_ALL+" known")
    elif choose1 == "1" : 
        c = int(input("[+] Enter ciphertext : "))
        dp = int(input("[+] Enter dp : "))
        dq = int(input("[+] Enter dq : "))
        p = int(input("[+] Enter p : "))
        q = int(input("[+] Enter q : "))
        CRTRSA(c,dp,dq,p,q)
