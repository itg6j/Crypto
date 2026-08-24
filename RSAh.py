from math import isqrt,gcd
import time 
import random 
import sys
import secrets
def decryption(cipher, d, n):
    decrypted_blocks, h, s = sam(cipher, d, n)
    message = b""
    byte_length = (n.bit_length() + 7) // 8  
    for num in decrypted_blocks:
        block = num.to_bytes(byte_length, 'big')
        block = block.lstrip(b'\x00')
        message += block
    return message, h, s
def decode(cipher, d, n):
    c = str(cipher)
    BlockSize = len(str(n))
    cipher_list = []
    for i in range(0, len(c), BlockSize):
        block_str = c[i:i+BlockSize]
        cipher_list.append(int(block_str))
    message,h,s = decryption(cipher_list,d,n)
    return message.decode('ascii', errors='ignore').rstrip(),h,s
def encryption(en,e,n):
    m = encode(en) 
    blocks=[]
    max_bytes = (n.bit_length() - 1) // 8
    BlockSize = max(1, max_bytes)
    for i in range(0,len(m),BlockSize):
        block = m[i:i+BlockSize]
        count = 0
        if len(block)<BlockSize: 
            count = BlockSize - len(block)
            block = block + (' ' * count).encode('utf-8')
        num = int.from_bytes(block,'big')
        if num>= n : 
            print("[+] message greater then modulus")
            sys.exit()
        blocks.append((num))
    cipher , count1 , status = sam(blocks,e,n)
    return cipher,count1,status
# encode ascii int , count padding  
def encode(message) : 
    m = message.encode('ascii')
    return m
# sam1: c or m count and padding  |||| count1 : num of square , ,multiplication and if == pow
def sam(base,exp,mod): 
    e = bin(exp)[2:]
    count2 = 0
    square = 0
    multipliction = 0
    isTrue=[]
    sam1=[]
    count1 = []
    for num in base : 
        x = 1
        for i in e: 
            x = (x**2) % mod
            count2 = count2 +1
            square=square+ 1
            if i == '1': 
                x = (x * num) % mod
                multipliction=multipliction+1
        if pow(num,exp,mod) == x : 
            isTrue.append(True)
        else : 
            isTrue.append(False)
        sam1.append((x))
    if all(isTrue) == True:   
        count1.append((square,multipliction,True))
    else : 
        count1.append((square,multipliction,False))
    if count2 == square : 
        return sam1, count1, True
    else : 
        return  sam1, count1, False
def isPrime(n) : 
    if n <=1 : 
        return False
    for i in range(2, int(n**0.5)+1) : 
        if n %i == 0 : 
            return False 
    return True
#result inverse 
def extendEuclidean(a,b,phi): 
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
    d = s1 % phi
    return(d)
def Euler1(number) : 
    if number == 1 : 
        return 0 
    else : 
        return number-1
def Euler2 (number1,number2) : 
    z = GCD1(number1,number2)
    if number1 == number2 and z == False : 
        return (number1-1)*number2
    if number1!=number2 and z == True: 
        z = Euler1(number1)
        u = Euler1(number2)
        b = u*z
        return b 
def GCD1(number1,number2) : 
    x = gcd(number1,number2)
    if x == 1 : 
        return True
    else : 
        return False
def RSAKEY(p,q) : 
    if isPrime(p) == True and isPrime(q) == True : 
        n = p*q
        phi =Euler2(p,q)
        e = 65537
        if gcd(e, phi) != 1:
            for i in range(2,phi):
                if 1<i and i<phi and gcd(phi,i) == 1 :
                    e = i 
                    break
        d= extendEuclidean(e,phi,phi)
        x = (d*e)%phi 
        if x == 1 : 
            return[n,phi,e,d,True]
        else : 
            return [n,phi,e,d,False]     
    else : 
        return"[-] factor is not prime"
def trialDivision(n):
    start_time = time.time()  
    timeout = 5 
    x = isqrt(n)
    p=x
    q=x
    while True:
        if n % p == 0 :
            break
        p=p+1
    while True:
        if n % q == 0:
            break
        q=q-1
    return p,q
def PollardRho(n): 
    a = 2
    b = 2
    d = 0
    while True:
        a = ((a**2)+1) %n
        b = ((b**2)+1) %n
        b = ((b**2)+1) %n
        d = gcd(abs(a-b),n)
        if 1<d<n and d != 1 : 
            p = d
            q = n//d
            return p,q
def generateRandomPrime(bits) : 
    while True : 
        x = (secrets.randbits(bits) | (1<<(bits-1)))|1
        if isPrime(x) : 
            return x
choose1 = input("[+] Do you want encryption or decryption ? e/d : ")
if choose1 == 'e' : 
    choose3 = input("[+] Do you want to encrypt it with your public key or with another key? 0/1: ")
    if choose3 == "0" : 
        e = int(input("[+] Enter encryption key : "))
        n = int(input("[+] Enter n : "))
        mc = input("[+] Enter message : ")
    else: 
        choose = input("[+] Do you want change factor  or generate random prime number you determine  of factor? y/n/g : ")
        if choose == 'y' : 
            p1 = int(input("[+] write first factor : "))
            q1 = int(input("[+] write second factor : "))
            p = p1
            q = q1
        elif choose == 'n' : 
            p = 2097143
            q = 2097169
        else : 
            size= int(input("[+] what size do you want such as 10 mean 10bits for one factor: "))
            p = generateRandomPrime(size)
            q = generateRandomPrime(size)
        mc = input("[+] Enter message : ")
        key = RSAKEY(p,q)
        n = key[0]
        phi = key[1]
        e = key[2]
        d = key[3]
        cipher,count,status = encryption(mc,e,n)
        x = "".join([str(c) for c in cipher])
        print(f"[+] prime number is {p} , {q}")
        print(f"[+] the encryption key is : {e}")
        print(f"[+] the dencryption key is : {d}")
        print(f"[+] the modula n {n}")
        print("[+] is e equal d ?:",key[4])
    cipher,count,status = encryption(mc,e,n)
    x = "".join([str(c) for c in cipher])
    print(f"[+] ciphertext : {x}")
elif choose1 == "d" : 
    d = int(input("[+] Enter  d decryption key: "))
    n = int(input("[+] Enter n modula : "))
    cipher = int(input("[+] Enter ciphertext : "))
    plain,count,status = decode(cipher,d,n)
    print(f"[+] plaintext : {plain}")
print("\n"*3,"-"*85,"\n"*3)
print("[+] Is equal pow with Square-and-Mulltiply algortihm and ? ",count[0][2])
print(f"[+] round of square : {count[0][0]} and multiplication : {count[0][1]}")
print("[+] count with the bit length of the exponent ? :",status)
timestr = time.time()
factor1,factor2 = trialDivision(n)
timeend= time.time()
time4 = timeend-timestr
print(f"[+] The factor from attack Trial Division is p = {factor1} q = {factor2} the time take{time4: .6f}s")
timestr1 = time.time()
factor1,factor2 = PollardRho(n)
timeend1 = time.time()
time4 = timeend1-timestr1
print(f"[+] The factor from attack Pollard rho is p = {factor1} q = {factor2}the time take{time4: .6f}s")
print(f"{'Bit Size':<10} | {'Trial Division (s)':<20} | {'Pollard Rho (s)':<20}")
print("-" * 55)
for bits in [20, 30, 40, 50]:
    half = bits // 2
    while True:
        pTest = random.getrandbits(half)
        if isPrime(pTest):
            break
    while True:
        qTest = random.getrandbits(half)
        if isPrime(qTest) and pTest != qTest:
            break      
    nTest = pTest * qTest
    actual_bits = nTest.bit_length()
    timestr= time.time()
    trialDivision(nTest)
    timeend = time.time() - timestr
    timestr = time.time()
    PollardRho(nTest)
    time5 = time.time() - timestr
    print(f"[+] {actual_bits:<10} | {timeend:<20.6f} | {time5:<20.6f}")
