for i in range(100, 1000):  # Цикл в котором 'i' принимает значение от 100 до 999
    a1 = i // 100  # Разбиваем 'i' на символы
    a2 = i % 100 // 10
    a3 = i % 100 % 10
    if ((a1 ** 3) + (a2 ** 3) + (a3 ** 3)) == i:  # Проверяем принадлежность к числам Армстронга
        print(i)  # Выводим 'i'
