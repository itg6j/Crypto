from Crypto.Util.number import *
def Euler1(number) : 
    if number == 1 : 
        return 0 
    x = is_prime(number)
    if x == False : 
        print("is not prime")
    if x == True : 
        return number-1
def Euler2 (number1,number2) : 
    x = is_prime(number1)
    y = is_prime(number2)
    z = GCD1(number1,number2)
    if number1 == number2 and x== True and y == True and z == True : 
        return (number1-1)*number2
    if number1!=number2 and x == True and y == True and z == True: 
        z = Euler1(number1)
        u = Euler1(number2)
        b = u*z
        return b 
def GCD1(number1,number2) : 
    x = GCD(number1,number2)
    if x == 1 :
        print("GCD : ",x) 
        return True
    else : 
        return False
def is_prime(number) : 
    if number <=1:
        print("number : ",number," is not prime")
        return False
    for i in range(2, int(number**0.5)+1) : 
        if number % i == 0 :
            print("number : ",number," is not prime")
            return False
    print("number : ",number," is prime")
    return True

x = Euler2(7,11)
print(x)
