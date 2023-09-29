# Задача 19. Замена
# В таблице a[1:100] записаны нули и единицы.
# Заменить 0 на 1, а 1 на 0.

import random

a = [0] * 100

for i in range(100):
    a[i] = random.randint(0, 1)
    print(a[i], end='')

print()

for i in range(100):
    a[i] = 1 - a[i]
    print(a[i], end='')
