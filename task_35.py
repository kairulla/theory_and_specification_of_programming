# Задача 35. Найти минимальный элемент двумерного массива.

import random

m = 10
n = 5
a = [[0] * n for _ in range(m)]
Min = 0

for i in range(m):
    for j in range(n):
        a[i][j] = random.randint(-10, 19)

for i in range(m):
    for j in range(n):
        print("{:4d}".format(a[i][j]), end="")
    print()

Min = a[0][0]

for i in range(m):
    for j in range(n):
        if a[i][j] < Min:
            Min = a[i][j]

print('Минимальный элемент двумерного массива', Min)
