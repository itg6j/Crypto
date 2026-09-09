from Crypto.Util.number import isPrime
p = int(input("[+] Enter modulus : "))
if isPrime(p) == False: 
    print("[+] Not Prime")
    exit()
solution = (p - 1) // 2
print(f"[+] you have solution : {solution}")
list1 = []
list2 = []
for i in range(1, p): 
    list1.append(i)
    x = (i * i) % p
    list2.append(x)
qr = sorted(set(list2))
qnr = [i for i in list1 if i not in qr]
print(f"[+] Quadratic Residues ({len(qr)}): {qr}")
print(f"[+] Quadratic Non-Residues : {qnr}")
