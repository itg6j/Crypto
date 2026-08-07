key = "1010000010"
P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
x = "".join([key[i-1] for i in P10])
num1 = x[0:5]
num2 = x[5:10]
left1 = num1[1:]+num1[0]
left2 = num2[1:]+num2[0]
num3 = left1+left2
key1 = "".join([num3[i-1] for i in P8])
print("This is key 1 : ",key1)
left3 = left1[2:]+left1[0:2]
left4 = left2[2:]+left2[0:2]
num4 = left3+left4
key2 = "".join([num4[i-1]for i in P8])
print("This is key 2 : ",key2)
