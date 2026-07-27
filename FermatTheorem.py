def fermat(number,exponent,prime) : 
    x = exponent % (prime-1)
    result  = pow(number,x,prime)
    return result
y = fermat(4,532,11)
print("result :",y)