def CommonModulus(set2) :
    commonM = 1 
    for i in set2 : 
        commonM = commonM*int(i)
    return commonM
def CommonModula (Common1,Common): 
    Common2 = 1
    list1 = []
    for i in Common1:
        Common2 = Common / int(i)
        list1.append(Common2)
    return list1
def inverse(list1,set2):
    list2 = []
    y = list(zip(list1,set2))
    for i,j in y : 
        num = 1 
        while True:
            x = (i*num)%int(j)
            if x == 1.0 : 
                list2.append(num)
                break
            num+=1
    return list2
def findx(Common,Common2,inverse1,set1) : 
    a = list(zip(Common2,inverse1,set1))
    list1 = []
    for y,z,x in a : 
        x = int(x)*y*z
        list1.append(x)
    r= 0
    for i in list1 : 
        r=r+i 
    u = int(r)%Common
    return u 
numberOfModulus = int(input("how much modulus : "))
print(numberOfModulus)
set1 = []
set2 = []
for i in range(0,numberOfModulus): 
    a = input("Enter a : ")
    m = input("Enter m : ")
    set1.append(a)
    set2.append(m)
Common = CommonModulus(set2)
Common2 = CommonModula(set2,Common)
inverse1 = inverse(Common2,set2)
x = findx(Common,Common2,inverse1,set1)
print("The answer : ",x)