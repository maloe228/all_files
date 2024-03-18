a = list(input())
n = a.index('!')
a.pop(n)
a.insert(n, '.')

for i in a:
    print(i)
