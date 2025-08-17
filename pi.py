import math
x = 2*math.sqrt(2)/9801
n = int(input("Enter value of n: "))
i = 0
total = 0
for i in range(0,n):
    y = math.factorial(4*i)
    z = 1103 + 26390*i
    a = math.pow(math.factorial(i),4)
    b = math.pow(396, 4*i)
    c = (x*(y*z))/(a*b)
    i += 1
    total += c
print(1/total)
