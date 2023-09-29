# Задача 21. Сумма ряда
# Даны натуральное n и вещественное a. Вычислить s, если x = a, s = 0.
# x = x * (a + i)
# s = s + 1 / x

a = float(input('a=...'))
n = int(input('n=...'))
x = a
s = 0

for i in range(n+1):
    x = x * (a + i)
    s = s + 1 / x

print('s=', s)
