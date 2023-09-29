# Задача 30. Самая длинная цепочка
# Дана вещественная таблица a[1], a[2],...,a[1000].
# Определить максимальное количество
# подряд идущих положительных элементов последовательности,
# не прерываемых ни нулями,
# ни отрицательными элементами.
# Напечатать найденный фрагмент.

import random

max = 100  # сколько элементов в массиве
a = [0] * max  # исследуемый массив
maxstart, maxstop, i, length, start, stop = 0, 0, 0, 0, 0, 0

random.seed()  # заполняем массив случайными числами
for i in range(max):
    a[i] = random.randint(0, 4)
    a[i] -= 1  # чтобы были числа меньше 0
    print(a[i], end='    ')

i = 0
while i < max:
    while i < max and a[i] <= 0:  # ищем начало фрагмента...
        i += 1
    start = i  # запоминаем начало фрагмента
    while i < max and a[i] > 0:  # ищем конец фрагмента
        i += 1
    stop = i - 1  # запоминаем конец фрагмента
    if length < stop - start:
        # текущий фрагмент длиннее всех предыдущих
        length = stop - start
        maxstart = start
        maxstop = stop

print()
if maxstop == 0:
    print('Нет положительных элементов')
else:
    print('Найдена последовательность от', maxstart, 'до', maxstop)
    for i in range(maxstart, maxstop + 1):
        print(a[i], end=' ')
