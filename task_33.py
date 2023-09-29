# Задача 33. Счастливые билеты
# На интервале (1000;9999) найти все простые числа,
# каждое из которых обладает тем свойством,
# что сумма первой и второй цифры записи этого числа
# равна сумме третьей и четвертой цифр.

m, n, i = 0, 0, 0

def Summ(x):
    s = 0
    y = x
    while y != 0:
        k = y % 10
        y = y // 10
        s = s + k
    return s

def Prost(x):
    ok = False
    i = 0
    if x == 2:
        ok = True
    elif not x % 2:
        ok = False
    else:
        ok = True
        i = 3
        while ok and i * i <= x:
            ok = x % i != 0
            i = i + 2
    return ok

for i in range(1000, 10000):
    if Prost(i):
        m = i // 100
        n = i % 100
        if Summ(m) == Summ(n):
            print(i)
