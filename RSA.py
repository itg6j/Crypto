from Crypto.Util.number import GCD
p = 53
q = 61
n = p*q
phi = (p-1)*(q-1)
for i in range(3,phi) : 
    if GCD(phi,i) == 1: 
        e = i
        break
print("encryption key = ",e)
m = "a"
m1 = ord(m)
d = pow(e,-1,phi)
print("d (inverse key) = ",d)
c = pow(m1,e,n)
print("ciphertext : ",c)
m = pow(c,d,n)
print("message : ",chr(m))