from Crypto.Util.number import * 

def GCD1(a,b) : 
    x = GCD(a,b)
    return x
a = 12
b = 18
y = a*b
z = y/GCD1(a,b)
print(z)