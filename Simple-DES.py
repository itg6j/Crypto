P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
EX1 = [4,3,2,1]
Sb1 = [[1,0,3,2],
      [3,2,1,0],
      [0,2,1,3],
      [3,1,3,2]]
Sb2 = [[0,1,2,3],
      [2,0,1,3],
      [3,0,1,0],
      [2,1,0,3]]
P4 = [1,3,4,2]
EP1 = [4, 1, 2, 3, 2, 3, 4, 1]
IPInv=[6,8,2,7,5,3,1,4]
def GenerationKey(masterKey) : 
    listSubKey=[]
    x = "".join([masterKey[i-1] for i in P10])
    num1 = x[0:5]
    num2 = x[5:10]
    left1 = num1[1:]+num1[0]
    left2 = num2[1:]+num2[0]
    num3 = left1+left2
    key1 = "".join([num3[i-1] for i in P8])
    listSubKey.append(key1)
    left3 = left1[2:]+left1[0:2]
    left4 = left2[2:]+left2[0:2]
    num4 = left3+left4
    key2 = "".join([num4[i-1]for i in P8])
    listSubKey.append(key2)
    return listSubKey
def EP(RE):
    x = "".join([RE[i-1]for i in EP1 ])
    return x
def XOR(Expand,subkey) : 
    e = (Expand)
    k = subkey[0]
    x = "".join(['1' if i!= j else '0' for i,j in zip(e,k)])
    subKey.pop(0)
    return x
def SBOX(x):
    S0 = x[:4]
    S1 = x[4:]
    row1 = int(S0[0] + S0[3], 2)
    col1 = int(S0[1] + S0[2], 2)
    row2 = int(S1[0] + S1[3], 2)
    col2 = int(S1[1] + S1[2], 2)
    sb1 = format(Sb1[row1][col1], '02b')
    sb2 = format(Sb2[row2][col2], '02b')
    return sb1 + sb2
def P4straight(SBOX) : 
    x = "".join([SBOX[i-1]for i in P4])
    return x
def XORL(LE,straight) : 
    x = "".join(['1' if i!= j else '0' for i,j in zip(LE,straight)])
    return x
def round(XORLE1,RE) : 
    round = XORLE1+RE
    return round
def swap1(XORLE1,RE) : 
    LE2 = RE
    RE2 = XORLE1
    return LE2,RE2
def IP_inverse(bits):
    return "".join([bits[i-1] for i in IPInv])
key = "1010000010"
plaintext = "10011010"
LE = plaintext[0:4]
RE = plaintext[4:8]
subKey = GenerationKey(key)
Expand = EP(RE)
xorEPK = XOR(Expand,subKey)
Sbox = SBOX(xorEPK)
straight = P4straight(Sbox)
XORLE = XORL(LE,straight)
round1 = round(XORLE,RE)
LE2 , RE2 = swap1(XORLE,RE)
Expand2 = EP(RE2)
xorEPK2 = XOR(Expand2, subKey) 
Sbox2 = SBOX(xorEPK2)
straight2 = P4straight(Sbox2)
XORLE2 = XORL(LE2, straight2)
round2 = XORLE2 + RE2
ciphertext = IP_inverse(round2)
print("ciphertext is : ",ciphertext)