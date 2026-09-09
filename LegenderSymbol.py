from Crypto.Util.number import isPrime
p = int(input("[+] Enter modulus : "))
if isPrime(p) == False : 
    print("[+]Not Prime")
    exit()
soultion = (p-1)//2
print("[+] soultion :",soultion)
list1= []
for i in range(1,p):
    x = pow(i,(p-1)//2,p)
    if x == 1 : 
        list1.append(i)
print("[+] the Quadritic Residue :",list1)
