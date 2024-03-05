from random import *

b = [randint(1, 100) for n in range(100)]

s = 0

for i in b:
    if i <= 20:
        s += i
print(s)  
