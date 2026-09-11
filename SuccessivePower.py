from sympy import isprime
powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
basis = [x for x in range(100,1000) if isprime(x)]
for p in basis:
    for x in range(1,p):
        for i,power in enumerate(powers):
            if i == len(powers)-1 : 
                print(p,x)
            elif not (x*power)%p == powers[i+1]:
                break
