from Crypto.Util.number import * 

def GCD1(a,b) : 
    x = GCD(a,b)
    if x ==1 : 
        print("Coprime")
    else : 
        print("This is not relatively prime")
GCD1(35,6)