from random import *

j = int(input())  # ввод с клавиатуры
g = [int(input()) for k in range(1, j)]

s = input().split()

a = [random() for i in range(100)]
b = [randint(1, 100) for n in range(1000)]

b.append(int(input()))  # добавить в конец строки
b.insert(1, 4653)  # поставить '4653' 2 элементом в списке
b.pop(0)  # удалить эл по номеру или последний, если ' '
b.remove(4653)  # удаление эл по значению

print(len(a))  # вывод длинны
print(a)  # вывод списка
print(*s)  # вывод через пробел
