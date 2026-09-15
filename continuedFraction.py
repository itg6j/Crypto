a = int(input("[+] Enter first number : "))
b = int(input("[+] Enter second number : "))
d=[]
k = []
while True : 
    q = a//b 
    d.append(q)
    r = a%b
    k.append(r)
    a = b 
    b = r
    print(q)
    if r == 0 : 
        break 
print("quotient :",d)
print("reminder :",k)
