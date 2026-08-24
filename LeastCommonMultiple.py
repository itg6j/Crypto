from math import gcd
from functools import reduce 
number = []
num = int(input("[+] Enter range : "))
multiple = 1
for i in range(0,num) : 
    x = int(input(f"[+] Enter number {i+1} : "))
    number.append(x)
def lcm(a, b):
    return a * b // gcd(a, b)
y = reduce(lcm,number)
print(f"[+] LCM = {y}")
