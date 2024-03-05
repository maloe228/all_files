from random import *

b = [randint(1, 100) for n in range(1000)]

for i in range(1, 999, 2):
    print(b[i])
