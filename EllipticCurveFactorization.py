from sage.all import * 
n = int(input("[+] Enter number modulus : "))
x = ecm.factor(Integer(n))
z = 0
for i in x : 
    z = z +1
    print(f"[+] The facotr num of {z} is : {i}")
print(f"[+] number of factor is : {z}")
phi = 1
for i in x : 
    phi *= (i-1)
print(f"[+] The Euler's is : {phi}")
