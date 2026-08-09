P10 = [3,5,2,7,4,10,1,9,8,6]
IP = [2, 6, 3, 1, 4, 8, 5, 7]
P8 = [6,3,7,4,8,5,10,9]
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
count = 0
def initialPermutation(plaintext): 
    return "".join([plaintext[i-1]for i in IP])
def GenerationKey(masterKey) : 
    listSubKey=[]
    #Permutation 10
    x = "".join([masterKey[i-1] for i in P10])
    num1 = x[0:5]
    num2 = x[5:10]
    # left 1 
    left1 = num1[1:]+num1[0]
    left2 = num2[1:]+num2[0]
    num3 = left1+left2
    # permuation 8
    key1 = "".join([num3[i-1] for i in P8])
    listSubKey.append(key1)
    #left 2 
    left3 = left1[2:]+left1[0:2]
    left4 = left2[2:]+left2[0:2]
    num4 = left3+left4
    # permuation 8 
    key2 = "".join([num4[i-1]for i in P8])
    listSubKey.append(key2)
    return listSubKey
def EP(RE):
    # Expand 
    x = "".join([RE[i-1]for i in EP1 ])
    return x
def XOR(Expand,subkey) : 
    e = Expand
    if count == 0 : 
        k = subkey[0]
    else : 
        k = subkey[1]
    #XOR 
    x = "".join(['1' if i!= j else '0' for i,j in zip(e,k)])
    return x
def SBOX(x):
    S0 = x[:4]
    S1 = x[4:]
    row1 = int(S0[0] + S0[3], 2)#row
    col1 = int(S0[1] + S0[2], 2)#column
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
plaintext = "01110010"
initial = initialPermutation(plaintext)
LE = initial[0:4]
RE = initial[4:8]
subKey = GenerationKey(key)
print ("subKey : ",subKey)
Expand = EP(RE)
print("Expand round 1 : ",Expand)
xorEPK = XOR(Expand,subKey)
print("XOR with sub key : ",xorEPK)
Sbox = SBOX(xorEPK)
print("Sbox round 1 s0 : ",Sbox[0:2],"S1 :",Sbox[2:4])
straight = P4straight(Sbox)
print("stright round 1 : ",straight)
XORLE = XORL(LE,straight)
print("XOR round 1  : ",XORLE)
round1 = round(XORLE,RE)
print("RE1 : ",round1)
LE2 , RE2 = swap1(XORLE,RE)
print("LE2 : ",LE2)
print("RE2 : ",RE2)
Expand2 = EP(RE2)
print("Expand round2: ",Expand2)
count +=1
xorEPK2 = XOR(Expand2, subKey) 
print("XOR round2 : ",xorEPK2)
Sbox2 = SBOX(xorEPK2)
print("Sbox round 2 s0 : ",Sbox2[0:2],"S1 :",Sbox2[2:4])
straight2 = P4straight(Sbox2)
print("straight round2 : ",straight2)
XORLE2 = XORL(LE2, straight2)
print("XOR with LE1 : ",XORLE2)
round2 = XORLE2 + RE2
print("swap round2 : ",round2)
ciphertext = IP_inverse(round2)
print("ciphertext is : ",ciphertext)
