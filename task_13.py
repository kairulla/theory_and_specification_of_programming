# Задача 13 МаксиЭлемент
# Дана целочисленная прямоугольная таблица А[1:100,1:50].
# Найдите наибольшее из чисел, встречающихся в этой таблице.

import random

m = 10
n = 5
a = [[0] * n for _ in range(m)]
Max = 0

for i in range(m):
    for j in range(n):
        a[i][j] = random.randint(-10, 19)

for i in range(m):
    for j in range(n):
        print("{:4d}".format(a[i][j]), end="")
    print()

Max = a[0][0]

for i in range(m):
    for j in range(n):
        if a[i][j] > Max:
            Max = a[i][j]

print('Максимальный элемент таблицы равен', Max)
