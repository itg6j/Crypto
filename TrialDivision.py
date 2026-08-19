from math import isqrt
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True
n = 2077
x = isqrt(n)
p=x
q=x
while True:
    if n % p == 0 and is_prime(p):
        break
    p=p+1
while True:
    if n % q == 0 and is_prime(q):
        break
    q=q-1
print(p, q)