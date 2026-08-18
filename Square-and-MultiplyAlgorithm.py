b = 4
e = 13
n = 49
bits = bin(e)[2:]
x = 1
for i in bits : 
    x = (x * x) % n
    if i == '1':
        x = (x * b) % n
print(x)