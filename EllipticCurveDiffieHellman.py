from sys import exit
import galois
from sympy import isprime
def additionPoint(x1, y1, x2, y2, a, p):
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
def scalar_multiplication(k, x, y, a, p):
  res_x, res_y = None, None 
  temp_x, temp_y = x, y
  while k > 0:
    if k & 1:  
        res_x, res_y = additionPoint(res_x, res_y, temp_x, temp_y, a, p)
    temp_x, temp_y = additionPoint(temp_x, temp_y, temp_x, temp_y, a, p)
    k >>= 1
  return res_x, res_y
p = int(input("[+] Enter GF (galois field): "))
if not isprime(p):
  print("[+] Error: p must be prime")
  exit()
if p <= 3:
  print("[+] Error: p is too small")
  exit()
GF = galois.GF(p)
a1 = int(input("[+] Enter a : "))
b1 = int(input("[+] Enter b : "))
if a1 >= p or b1 >= p:
  print("[+] Error: Coefficients a and b must be in the field (< p)")
  exit()
print("\n--- Base Point Setup ---")
px = int(input("[+] Enter Base Point x (P_x): "))
py = int(input("[+] Enter Base Point y (P_y): "))
if (py**2) % p != ((px**3) + a1 * px + b1) % p:
  print("[+] Error: Base Point P is not on the curve!")
  exit()
print("\n--- Key Exchange Simulation ---")
xa = int(input("[+] Enter Alice's private key (k_pr,A): "))  # في المثال = 3
xb = int(input("[+] Enter Bob's private key (k_pr,B): "))  # في المثال = 10
Ax, Ay = scalar_multiplication(xa, px, py, a1, p)
print(f"[+] Alice Public Key  (A = {xa}*P): ({Ax}, {Ay})")
Bx, By = scalar_multiplication(xb, px, py, a1, p)
print(f"[+] Bob Public Key    (B = {xb}*P): ({Bx}, {By})")
Tab_Alice_x, Tab_Alice_y = scalar_multiplication(xa, Bx, By, a1, p)
Tab_Bob_x, Tab_Bob_y = scalar_multiplication(xb, Ax, Ay, a1, p)
print("\n--- Shared Secret Calculation ---")
print(f"[+] Alice calculates Tab = {xa} * B = ({Tab_Alice_x}, {Tab_Alice_y})")
print(f"[+] Bob calculates   Tab = {xb} * A = ({Tab_Bob_x}, {Tab_Bob_y})")
if (Tab_Alice_x, Tab_Alice_y) == (Tab_Bob_x, Tab_Bob_y):
  print(f"[+] Success! Shared Secret Key established: ({Tab_Alice_x}, {Tab_Alice_y})")
