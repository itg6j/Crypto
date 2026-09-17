import math 
num = int(input("[+] Enter hash bit length : "))
num1 = float(input("[+] Enter target probability percentage (e.g., 50) : "))
P = num1/100
space = 2**num
k = math.sqrt(2 * space * math.log(1 / (1 - P)))
print(f"[+] {math.ceil(k)}")
