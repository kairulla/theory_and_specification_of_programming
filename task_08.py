# Задача 8 Произведение
# Дано натуральное число N.
# Вычислить произведение первых N сомножителей.
# (2/1)*(2/3)*(4/3)*(4/5)/….

import math

res = 1.0
flag = 0
x = 2
y = 1

n = int(input("n=..."))

for i in range(1, n+1):
    res = res * x / y
    if flag == 0:
        y = y + 2
    else:
        x = x + 2
    flag = 1 - flag

print(res)
