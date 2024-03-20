a = input()
st = 0
for i in a:
    st += int(i)

print(st)




a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('yes')
else:
    print('no')




a = 10
for i in range(1, a + 1):
    print(i**2-10*i+2)



from random import *

b = [randint(-100, 100) for n in range(100)]

print(b)

s = 0

for i in b:
    if i > 0:
        s += i
print(s)  





f1 = f2 = 1

n = int(input())

print(f1, f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')







a = str(input())

b = int(a)**2
bm = list(str(b))

m = list(a)
k = len(m)

x = len(bm) - len(m)

while k > 0:
    if m[k-1] == bm[k-1+x]:
        k -= 1
    else:
        print('no')
        break
print('yes')








f = open('text.txt')

data = f.read()
print(data)

f.close()







63
70
51
