def Properties(a,b,n) : 
    x = ((a%n)+(b%n))%n
    y = ((a%n)-(b%n))%n
    z = ((a%n)*(b%n))%n
    print("Addition : ",x)
    print("Subtraction : ",y)
    print("multiplication : ",z)
Properties(1723345,2124945,11)