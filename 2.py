from random import random  # импорт модуля

n = int(input())  # ввод переменной

while n > 0:  # пока n > 0, вывести рандомное число и отнять от 'n' 1
    print(random() * 100)
    n -= 1
