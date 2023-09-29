# Задача 26. Подсчет чисел
# Дано 100 чисел от 1 до 50.
# Определить, сколько среди них чисел Фибоначчи
# и сколько чисел,
# первая значащая цифра в десятиричной записи которых 1 или 2

import random

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

def set_init():
    prost = set()
    m = 1
    flag = True
    while flag:
        f = fib(m)
        if f > 50:
            flag = False
        else:
            prost.add(f)
        m += 1
    return prost

prost = set_init()
random.seed()
a = [random.randint(0, 50) for _ in range(100)]
s = 0
x = 0
for i in range(100):
    if a[i] in prost:
        s += 1
    if a[i] // 10 == 1 or a[i] // 10 == 2:
        x += 1
    elif a[i] // 10 == 0:
        if a[i] % 10 == 1 or a[i] % 10 == 2:
            x += 1

print('В массиве', s, 'чисел Фибоначчи')
print('В массиве', x, 'элементов с 1 или 2 в начале')
