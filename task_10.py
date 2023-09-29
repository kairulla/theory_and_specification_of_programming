# Задача 10 Сумма 17-ти.
# Даны действительные числа x[1], x[2],..., x[17].
# Найти сумму значений | x[i] - x[j] | при условии, что 1 <= i < j <= 17.

import random

a = [0] * 17
s = 0

for i in range(17):
    a[i] = random.randint(0, 50)

for i in range(17):
    print(f"{a[i]:4}", end="")
print()

for i in range(17):
    for j in range(i):
        s += abs(a[i] - a[j])

print(s)