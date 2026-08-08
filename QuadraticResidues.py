p = 29 
numbers = [14, 6, 11]
for x in numbers:
    for a in range(1, p):
        if (a * a) % p == x:
            root1 = a
            root2 = p - a
            smaller_root = min(root1, root2)
            print("Quadratic Residues : ",x)
            print("roots : ",root1,root2)
            print("small root : ",smaller_root)
            break