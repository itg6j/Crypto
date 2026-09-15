a = int(input("[+] Enter first number : "))
b = int(input("[+] Enter second number : "))
list1=[]
while True : 
    q = a//b 
    list1.append(q)
    r = a%b
    a = b 
    b = r
    print(q)
    if r == 0 : 
        break 
print(list1)
