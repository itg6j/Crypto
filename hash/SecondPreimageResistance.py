import math
num = int(input("[+] Enter hash bit length : "))
num1 = float(input("[+] Enter target probability percentage (e.g., 50) : "))
percent = num1/100
space = 2**num
p = 1/space
try:
    k = math.log(1-percent)/math.log(1-p)
except Exception : 
    k = math.log(1 / (1 - percent)) * space
print(f"[+] number of attempts required to match a specific {math.ceil(k)}")
