from math import sqrt
p = int(input("[+] Enter number : "))
x = (p+1)-(2*sqrt(p))
y = (p+1)+(2*sqrt(p))
print(f"[+] Hasse's theorem guarantees that the number of points on this curve definitely falls within the range from {int(x)} to {int(y)}")