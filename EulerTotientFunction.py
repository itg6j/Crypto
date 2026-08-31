from math import gcd
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

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
x = Euler2(num1,num2)
print(f"The result  : {x}") 
