# Задача 3 Счастливые билеты.
# Написать программу определения количества билетов с 6-значными номерами,
# у которых сумма первых 3 десятичных цифр
# равна сумме 3 последних десятичных цифр

def summ(x):
    y = x
    l = 0
    while y != 0:
        k = y % 10
        y = y // 10
        l = l + k
    return l

count = 0
for j in range(1000000):
    w1 = j // 1000
    w2 = j % 1000
    if summ(w1) == summ(w2):
        count = count + 1
        print(j, '-->', count)