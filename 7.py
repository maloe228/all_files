from random import *

s1, s2 = int(input()), int(input())

b = [1,2,3,4,5,6,7,8,9,10]

a = [random() for i in range(100)]
print(sum(a[0:5]))

print(sum(b[(s1-1):s2])/(s2-s1+1))
