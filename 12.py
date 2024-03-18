for i in range(100, 1000):
    s = i // 100
    d = i % 100 // 10
    e = i % 100 % 10
    if (s**3 + d**3 + e**3) == i:
        print(i)
for i in range(1000, 10000):
    t = i // 1000
    s = i % 1000 // 100
    d = i % 1000 % 100 //10
    e = i % 1000 % 100 % 10
    if (t**4 + s**4 + d**4 + e**4) == i:
        print(i)
