import sys
from sympy import isprime
q = int(input("[+] Enter Prime modulus (p/q): "))
if not isprime(q):
    print("[-] Error: Modulus must be a prime number!")
    sys.exit()
alpha = int(input("[+] Enter primitive root (g/alpha): "))
print("\n--- Current Knowledge Setup ---")
has_Xa = input("[+] Do you know Alice's private key (Xa)? (y/n): ")
Xa = int(input("[+] Enter Alice's private key: ")) if has_Xa else None
has_Xb = input("[+] Do you know Bob's private key (Xb)? (y/n): ")
Xb = int(input("[+] Enter Bob's private key: ")) if has_Xb else None
if Xa is not None:
    A = pow(alpha, Xa, q)
else:
    A = int(input("[+] Enter Alice's Public Key (A): "))
if Xb is not None:
    B = pow(alpha, Xb, q)
else:
    B = int(input("[+] Enter Bob's Public Key (B): "))
print(f"\n[+] Alice Public Key (A): {A}")
print(f"[+] Bob Public Key (B): {B}")
k1 = pow(B, Xa, q) if Xa is not None else None
k2 = pow(A, Xb, q) if Xb is not None else None
if k1 is not None and k2 is not None:
    if k1 == k2:
        print(f"[+] Success! Keys match: {k1}")
    else:
        print("[-] Keys do not match! Check your inputs.")
elif k1 is not None:
    print(f"[+] Computed Shared Secret from Alice's side: {k1}")
elif k2 is not None:
    print(f"[+] Computed Shared Secret from Bob's side: {k2}")
else:
    print("[-] Infeasible: Need at least one private key to compute the shared secret.")
