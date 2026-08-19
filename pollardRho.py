from Crypto.Util.number import GCD 
n = 94417
a = 2
b = 2
d = 0
for i in range(n) : 
    a = ((a**2)+1) %n
    b = ((b**2)+1) %n
    b = ((b**2)+1) %n
    d = GCD((a-b),n)
    if 1<d and d<n and d != 1 : 
        print("p = : ",d)
        print("q = : ",n//d)
        n1 = d * (n//d)
        if n == n1 : 
            print("input equal output ? : ",True)
        break 
