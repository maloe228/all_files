from random import *

b = [randint(1, 100) for n in range(1000)]

for i in b:
    if i % 2 == 0:
        print(i)

    if i % 10 == 0:
        print(i)
