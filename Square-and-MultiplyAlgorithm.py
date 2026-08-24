b = int(input("[+] Enter base : "))
e = int(input("[+] Enter encryption key : "))
n = int(input("[+] Enter n : "))
bits = bin(e)[2:]
square = 0
multiplication = 0
x = 1
for i in bits : 
    x = (x * x) % n
    square = square +1
    if i == '1':
        x = (x * b) % n
        multiplication = multiplication +1
print(f"[+] The result is : {x}")
print(f"[+] Round of square : {square}")
print(f"[+] Round of multiplication : {multiplication}")
