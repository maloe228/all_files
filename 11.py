from random import *
N = 1000000
i = 0
d = [randint(1, 100) for n in range(N)]
print(d)

#a.sort()
# print(sorted(d)) сортировка выбором

while i < N - 1:
	m = i
	j = i + 1
	while j < N:
		if d[j] < d[m]:
			m = j
		j += 1
	d[i], d[m] = d[m], d[i]
	i += 1
print(d)


#пузырьки

def bubble_sort(x):
    for i in range(0,len(x)-1): 
        for j in range(len(x)-1): 
            if(x[j]>x[j+1]):  
                x[j], x[j+1] = x[j+1], x[j]
    return x
 
list1 = [5, 3, 8, 6, 7, 2] 
print(list1) 

print(bubble_sort(list1)) 


#пузырьки упростить

x = [5, 3, 8, 6, 7, 2] 
print(x)
for i in range(0,len(x)-1):
  for j in range(len(x)-1):
    if(x[j]>x[j+1]):
      x[j], x[j+1] = x[j+1], x[j]
print(x)
