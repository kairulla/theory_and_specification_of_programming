# Задача 37.
# В двумерном массиве целых чисел поменять местами элементы,
# симметричные относительно главной диагонали.

import random
def swap_diagonal_symmetric_elements(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            # Переставляем элементы симметрично относительно главной диагонали
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Пример использования
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

m = n = 6
matrix = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = random.randint(-10, 19)

print("\nдо преобразования")
for i, r in enumerate(matrix):
    for j, c in enumerate(r):
        print("%5d" % matrix[i][j], end="")
    print()

swap_diagonal_symmetric_elements(matrix)

# Вывод измененной матрицы
print("\nпосле преобразования")
for i, r in enumerate(matrix):
    for j, c in enumerate(r):
        print("%5d" % matrix[i][j], end="")
    print()

