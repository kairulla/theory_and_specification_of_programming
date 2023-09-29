# Задача 12 Среднее арифметическое
# m и n - натуральные числа, m<=n.
# Найти среднее арифметическое чисел
# a[1],... , a[m-1], a[m+1],... , a[n] (всех, кроме a[m]).

import random

max = 20
a = [0] * max
l = 0
s = 0.0

random.seed()

for i in range(max):
    a[i] = random.random() * max
    print(f"{a[i]:15.7f}")

l = int(input("l=..."))

s = 0.0
for i in range(max):
    if i + 1 != l:
        s += a[i]

s = s / (max - 1)
print(f"Среднее арифметическое всех чисел, кроме {l}, равно {s:15.7f}")
