def congruent(x,y,n):
    z = x%n
    t = y%n
    if z==t : 
        return True
    else : 
        return False

z = congruent (73,4,23)
print(z)