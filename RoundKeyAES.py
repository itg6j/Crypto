state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]
def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    list2 =[]
    for i in matrix: 
        x = chr(i)
        list2.append(x)
    for i in list2 : 
        print(i,end="")

def add_round_key(s, k):
    list1 = []
    for i,j in zip(s,k) : 
        for c,n in zip(i,j):
            f = c^n 
            list1.append(f)
    return list1
x = add_round_key(state,round_key)
print(x)
matrix2bytes(x)

