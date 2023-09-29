# Задача 16 Больше семи
# n - натуральное,
# a[1], a[2],..., a[n] - целые.
# Заменить все большие 7 члены последовательности числом 7.
# Найти количество таких членов.

import random

n = 100
a = [0] * n
count = 0

for i in range(n):
    a[i] = random.randint(0, 16)
    print(f"{a[i]:4}", end="")
print()

for i in range(n):
    if a[i] > 7:
        a[i] = 7
        count += 1
    print(f"{a[i]:4}", end="")
print(f"Всего {count}")