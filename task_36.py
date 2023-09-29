# Задача 36. Поменять местами в двумерном массиве 1 и 2 столбец.

# a = [
#     [0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 0]
# ]

import random

m = 6
n = 5
a = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        a[i][j] = random.randint(-10, 19)

print("\nдо преобразования")
for i, r in enumerate(a):
    for j, c in enumerate(r):
        print("%5d" % a[i][j], end="")
    print()

for i, r in enumerate(a):
    a[i][0], a[i][1] = a[i][1], a[i][0]

print("\nпосле преобразования")
for i, r in enumerate(a):
    for j, c in enumerate(r):
        print("%5d" % a[i][j], end="")
    print()
