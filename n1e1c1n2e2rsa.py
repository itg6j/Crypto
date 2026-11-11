from math import gcd

n1 = int(input("[+] Enter n1 : "))
e1 = int(input("[+] Enter e1 : "))
c1 = int(input("[+] Enter c1 : "))
n2 = int(input("[+] Enter n2 : "))
e2 = int(input("[+] Enter e2 : "))
p = gcd(n1, n2)
print("Shared prime found:", p != 1 and p != n1)
if p in (1, n1, n2):
    print("No nontrivial common factor found via gcd(n1,n2).")
else:
    q1 = n1 // p
    q2 = n2 // p
    print("p  =", p)
    print("q1 =", q1)
    print("q2 =", q2)
    assert p * q1 == n1
    assert p * q2 == n2
    phi1 = (p - 1) * (q1 - 1)
    d1 = pow(e1, -1, phi1)
    m1 = pow(c1, d1, n1)
    m1_bytes = m1.to_bytes((m1.bit_length() + 7) // 8, 'big')
    print("\nRecovered integer m1:", m1)
    print("As bytes:", m1_bytes)
    try:
        print("As text:", m1_bytes.decode('utf-8'))
    except UnicodeDecodeError:
        print("Not valid utf-8 text; printing hex instead:")
        print(m1_bytes.hex())
