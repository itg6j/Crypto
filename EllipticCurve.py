import galois
from sys import exit
from sympy import isprime
import plotext
from math import sqrt 
def additionPoint(x1,y1,x2,y2,a,p):
    if x1 is None:
        return x2, y2
    if x2 is None:
        return x1, y1
    if x1 == x2 and (y1 != y2 or y1 == 0):
        return None, None
    if x1 == x2 and y1 == y2:
        num = (3 * (x1**2) + a) % p
        den = (2 * y1) % p
        s = (num * pow(den, -1, p)) % p
    else:
        num = (y2 - y1) % p
        den = (x2 - x1) % p
        s = (num * pow(den, -1, p)) % p
    x3 = (s**2 - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3
print("[+] Do you want know just one point what inverse it or point Negation ??")
print("[+] Do you want all point  galois field ??")
print("[+] Do you want check if  the point at infinity ?? ")
print("[+] Elliptic Curve Discrete Logarithm Problem ")
print("[+] Do you want addition point ")
print("[+] Hasse's theorem the number of points on the curve is dentoted : ")
point = input("[+] Enter number 1,2 ... : ")
p = int(input("[+] Enter GF (galois field): "))
if isprime(p) == False: 
    print("[+] Not prime")
    exit
if p <= 3 : 
    print("[+] p is so small ")
    exit()
GF = galois.GF(p)
a1 = int(input("[+] Enter a : "))
b1 = int(input("[+] Enter b : "))
if a1>=p : 
    print("[+] Cofficient a larger modulus error must in field")
if b1>=p : 
    print("[+] Cofficient a larger modulus error must in field")
if point == "1".lower() : 
    x = int(input("[+] Enter x point : "))
    y = int(input("[+] Enter y point : "))
    inv_y = (p - y) % p
    print(f"[+] P + P = 0 or P + Q = 0 The inverse point or point Negation is ({x},{inv_y})")
    exit()
elif point == "2".lower() : 
    a = GF(a1)
    b = GF(b1)
    points = []
    xPoints = []
    yPoints = []
    for x_val in range(p):
        x = GF(x_val)
        rhs = x**3 + a*x + b    
        for y_val in range(p):
            y = GF(y_val)
            if y**2 == rhs:
                pt = (int(x), int(y))
                points.append(pt)
                xPoints.append(pt[0])
                yPoints.append(pt[1])
    inverses = {}
    for x, y in points:
        inv_y = (p - y) % p
        inverses[(x, y)] = (x, inv_y)
    print("\n" + "="*45)
    print(f"  Point P (x, y)   |   Inverse -P (x, (p-y)%p)  ")
    print("="*45)
    seen = set()
    for pt, inv in inverses.items():
        if pt not in seen:
            print(f"   ({pt[0]:2d}, {pt[1]:2d})       ---->      ({inv[0]:2d}, {inv[1]:2d})")
            seen.add(pt)
            seen.add(inv)
    print("="*45)
    print(f"total of point (without infinit point):  {len(points)}")
    print("="*45 + "\n")
    point1 = input("[+] Do you want Drawing this point y/n : ")
    if point1 == "y".lower() :
        try :  
            plotext.clf()
            plotext.plotsize(90, 25)
            plotext.scatter(xPoints, yPoints, marker="dot")
            ticks = list(range(0, p))
            plotext.xticks(ticks)
            plotext.yticks(ticks)
            plotext.title(f"Elliptic Curve over GF({p}): y^2 = x^3 + {a1}x + {b1} mod {p}")
            plotext.xlabel(f"X in GF({p})")
            plotext.ylabel(f"Y in GF({p})")
            plotext.theme("dark")
            plotext.show()
            exit()
        except Exception : 
            print("[+] Error")
    else : 
        exit()
elif point == "3" : 
    x = int(input("[+] Enter x first point : "))
    y = int(input("[+] Enter y first point : "))
    x1 = int(input("[+] Enter x second point : "))
    y1 = int(input("[+] Enter y second point : "))
    x3,y3 = additionPoint(x,y,x1,y1,a1,p)
    if x3 == None and y3 == None :
        print("[+] point at infinity")
        print(f"[+] first point P({x},{y})")
        print(f"[+] first point P({x1},{y1})")
        exit()
    else : 
        print(f"[+] The point is ({x3},{y3})")
elif point == "4" :
    x = int(input("[+] Enter x first point : "))
    y = int(input("[+] Enter y first point : "))
    x1 = int(input("[+] Enter x second point : "))
    y1 = int(input("[+] Enter y second point : "))
    count = int(input("[+] Enter number of round do you want : "))
    list1 = []
    x4 = (x1,y1)
    list1.append(x4)
    for i in range(count-1) : 
        x3,y3 = additionPoint(x,y,x1,y1,a1,p)
        x1 ,y1 = x3,y3 
        x4 = (x1,y1)
        list1.append(x4)
    count1 = 0
    print("\n")
    for i in list1 : 
        count1 = count1 + 1 
        print(f"[+] {count1}P = {i}")
elif point == "5" : 
    count = int(input("[+] Enter number of point : "))
    if count >=3 : 
            list1 = []
            x = int(input("[+] Enter x point : "))
            y = int(input("[+] Enter y point : "))
            for i in range(count-1) : 
                x1 = int(input("[+] Enter x point : "))
                y1 = int(input("[+] Enter y point : "))
                x3,y3 = additionPoint(x,y,x1,y1,a1,p)
                x , y = x3,y3
                print(f"[+] point is P({x},{y})")
    else :          
        x = int(input("[+] Enter x first point : "))
        y = int(input("[+] Enter y first point : "))
        x1 = int(input("[+] Enter x second point : "))
        y1 = int(input("[+] Enter y second point : "))
        x3,y3 = additionPoint(x1,y1,x1,y1,a1,p)
        print(f"[+] point is P({x3},{y3})")
elif point == "6" : 
    x = (p+1)-(2*sqrt(p))
    y = (p+1)+(2*sqrt(p))
    print(f"[+] Hasse's theorem the number of points on this curve definitely falls within the range from {int(x)} to {int(y)}")
