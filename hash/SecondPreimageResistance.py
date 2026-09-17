import math
num = int(input("[+] Enter hash bit length : "))
num1 = float(input("[+] Enter target probability percentage (e.g., 50) : "))
percent = num1/100
space = 2**num
p = 1/space
k = math.log(1-percent)/math.log(1-p)
print(math.ceil(k))
