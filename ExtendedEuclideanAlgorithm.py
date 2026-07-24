def extendEuclidean(a, b): 
    s1, s2 = 1, 0
    t1, t2 = 0, 1    
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        s = s1 - q * s2
        t = t1 - q * t2
        s1, s2 = s2, s
        t1, t2 = t2, t
    return a, s1, t1
num1 = 26513
num2 = 32321 
gcd, x, y = extendEuclidean(num1, num2) 
print("GCD =", gcd)
print("x =", x)
print("y =", y)