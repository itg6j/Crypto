q = 17
alpha = 2
Xa = 3
Xb = 5
b = pow(alpha,Xa,q)
a = pow(alpha,Xb,q)
k1 = pow(b,Xb,q)
k2 = pow(a,Xa,q)
if k1 == k2 : 
    print(f"[+] key is : {k1}")