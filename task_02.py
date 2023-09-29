# Задача 2 Длинная арифметика.
# Найти все цифры десятичной записи числа 3^2.

def Mult(data, c):
    s = data
    m = int(c)
    f = 0
    for i in range(len(s)-1, -1, -1):
        d = s[i]
        k = int(d)
        l = k * m + f
        d = str(l % 10)
        s = s[:i] + d + s[i+1:]
        f = l // 10
    if f > 0:
        d = str(f)
        s = d + s
    return s

a = int(input('Введите основание...'))
k = int(input('Введите показатель...'))
res = ''
s1 = str(a)
res = s1
n = len(s1)
for m in range(1, k):
    for i in range(n-1, -1, -1):
        s = Mult(res, s1[i])
        res = s
print(res)