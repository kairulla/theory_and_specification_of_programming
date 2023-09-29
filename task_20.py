# Задача 20. Таблица
# Дана целочисленная таблица A[1:1000].
# Подсчитайте наибольшее число идущих в ней подряд одинаковых элементов.

import random

n = 10
a = [0] * n
i = 0
k = 0
kvo = 0

for i in range(n):
    a[i] = random.randint(0, 2)

print(a)

kvo = 1
k = 1
for i in range(1, n):
    if a[i] != a[i-1]:
        k = 1
    else:
        k += 1
    if k > kvo:
        kvo = k

print('В массиве есть', kvo, 'одинаковых подряд идущих элементов')
