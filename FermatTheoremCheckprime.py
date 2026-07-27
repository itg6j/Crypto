def fermat(number,exponent,prime) : 
    x = exponent % (prime-1)
    result  = pow(number,x,prime)
    return result
def is_prime (prime):
    if prime<=1 : 
        return False
    for i in range(2,int(prime**0.5)+1) : 
        if prime%i == 0 :             return False
    return True 
prime = 11
c = is_prime(prime) 
if c == True : 
    y = fermat(4,532,prime)
    print("result :",y)
else : 
    print("not prime number")