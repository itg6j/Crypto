import galois
import plotext
p = int(input("[+] Enter GF (galois field): "))
GF = galois.GF(p)
a1 = int(input("[+] Enter a : "))
b1 = int(input("[+] Enter b : "))
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