# Задача 28. Поиск чисел.
# Написать программу,
# которая находит и выводит на печать все четырехзначные числа abcd,
# для которых выполняются следующие условия:
# 1) a, b, c, d - разные цифры
# 2) ab-cd=a+b+c+d

a, b, c, d = 0, 0, 0, 0
for a in range(1, 10):
    for b in range(0, 10):
        if a != b:
            for c in range(0, 10):
                if a != c and b != c:
                    for d in range(0, 10):
                        if a != d and b != d and c != d:
                            if a * b - c * d == a + b + c + d:
                                print(a, b, c, d, end='   ')
