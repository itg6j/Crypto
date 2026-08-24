from math import gcd
from functools import reduce 
num = int(input("[+] Enter num of range : "))
number = []
for i in range(0,num) : 
    x = int(input(f"[+] Enter number {i+1} : "))
    number.append(x)
y = reduce(gcd,number)
print("[+] The Grates Common Divisor : ",y)
