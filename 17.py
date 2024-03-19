f1 = 1
f2 = 1

n = int(input())

i = 0
while i < n - 2:
    sum = f1 + f2
    f1 = f2
    f2 = sum
    i += 1

print(f2)
