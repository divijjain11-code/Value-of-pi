import math
n = int(input("Enter the value of n: "))
i = int(0)
total = 0
for i in range(0,n):
    x = (math.pow(-1,i))/((2*i)+1)
    total += x
    i += 1
print(total*4)
