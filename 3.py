from random import random

n = 10
a1 = 0
a2 = 0
a3 = 0
a4 = 0

while n > 0:
    c = random()
    if (c >= 0) and (c < 0.25):
        a1 += 1
    if (c >= 0.25) and (c < 0.5):
        a2 += 1
    if (c >= 0.5) and (c < 0.75):
        a3 += 1
    if (c >= 0.75) and (c < 1):
        a4 += 1
    n -= 1
print('Точек в промежутке [0; 0,25) -', a1)
print('Точек в промежутке [0,25; 0,5) -', a2)
print('Точек в промежутке [0,5; 0,75) -', a3)
print('Точек в промежутке [0,75; 1) -', a4)
