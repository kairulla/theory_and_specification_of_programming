# Задача 18. Простые делители
# Найти все простые делители натурального числа n.

n = int(input('Введите число...'))
print('Делители числа', n, ':', end=' ')
i = 2
while n != 1:
    if n % i == 0:
        print(i, end=' ')
        while n % i == 0:
            n //= i
    i += 1