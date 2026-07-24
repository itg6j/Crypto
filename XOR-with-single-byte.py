from pwn import * 
cipher = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for key in range(256) : 
    y = xor(cipher,key).decode('utf-8',errors = 'ignore')
    if y[0:6] == 'crypto' : 
        print(y)
    