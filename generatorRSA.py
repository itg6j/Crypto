from Crypto.Util.number import getPrime, inverse, GCD
bits = 1024
p = getPrime(bits)
q = getPrime(bits)
while p == q:
    q = getPrime(bits)
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
if GCD(e, phi) != 1:
    e = 3
    while GCD(e, phi) != 1:
        e += 2
d = inverse(e, phi)
print(f"Prime p ({bits}-bit):\n{p}\n")
print(f"Prime q ({bits}-bit):\n{q}\n")
print(f"Modulus n:\n{n}\n")
print(f"Public Exponent e:\n{e}\n")
print(f"Private Exponent d:\n{d}\n")
