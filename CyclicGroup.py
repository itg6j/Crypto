from math import gcd
from factordb.factordb import FactorDB
def Euler1(number):
    if number == 1:
        return 1
    count = 0
    for i in range(1, number):
        if gcd(number, i) == 1:
            count += 1
    return count
def GCD1(number1, number2):
    return gcd(number1, number2) == 1
def Euler2(number1, number2):
    if GCD1(number1, number2):
        return Euler1(number1) * Euler1(number2)
    else:
        return Euler1(number1 * number2)
def factor(x) : 
    v = None
    f = FactorDB(x)
    f.connect()
    status = f.get_status()

    if status == "P":
        d = x - 1
        v = d

    if v != None:
        f2 = FactorDB(d)
        f2.connect()
        factor1 = f2.get_factor_list()
        status = "FF"
    if status == "FF":
        if v == None:
            factor1 = f.get_factor_list()
        list1 = []
        for i in (factor1) : 
            if i not in list1 : 
                list1.append(i)
        return list1
def cyclicGroup(f,phi,a) : 
    list1 =[]
    result = []
    for i in range(1,a+1) : 
        x=gcd(i,a) 
        if x == 1 : 
            list1.append(i)   
    eu = Euler2(len(list1),1)
    for g in list1:
        is_generator = True
        for q in f:  
            b = phi // q  
            if pow(g, b, a) == 1:
                is_generator = False
                break
        if is_generator:
            result.append(g)
    return result
choose = input("[+] you know modulus y/n ?? ")
if choose == 'y' : 
    num1 = int(input("[+] Enter modulus : "))
    x = Euler2(num1, 1)      
    f = factor(x)             
    j = cyclicGroup(f, x, num1)
    
else : 
    num1 = int(input("[+] Enter number 1 : "))
    num2 = int(input("[+] Enter number 2 : "))
    x = Euler2(num1,num2)
    f = factor(x)             
    j = cyclicGroup(f, x, num1)
print(f"[+] Generator is {j}")