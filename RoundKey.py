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


def add_round_key(s, k):
    list1 = []
    for i,j in zip(s,k) : 
        for u,h in zip(i,j) : 
            x = u^h
            list1.append(x)
    return list1
def matrix2bytes(x) : 
    for i in x : 
        print(chr(i),end="")
x = add_round_key(state, round_key)
matrix2bytes(x)

