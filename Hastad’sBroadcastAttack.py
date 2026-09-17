import gmpy2
from itertools import combinations
from Crypto.Util.number import long_to_bytes, inverse
nlist = []
clist = []
num = int(input("[+] Enter total number of (n, c) pairs you have: "))
e = int(input("[+] Enter public key : "))
for i in range(num):
    n = int(input(f"[+] Enter modulus : "))
    c = int(input(f"[+] Enter ciphertext : "))
    nlist.append(n)
    clist.append(c)
found = False
for grp in combinations(zip(nlist, clist), e):
    N = 1
    for x in grp:
        N *= x[0]
    M = 0
    for x in grp:
        ni, ci = x[0], x[1]
        Ni = N // ni
        try:
            ui = inverse(Ni, ni)
            M = (M + ci * ui * Ni) % N
        except ValueError:
            break
    else:
        m, exact = gmpy2.iroot(M, e)
        if exact:
            print("[+] Flag / Message:", long_to_bytes(int(m)).decode('utf-8', errors='ignore'))
            found = True
            break
if not found:
    print("\n[-] No valid combination produced an exact root.")
