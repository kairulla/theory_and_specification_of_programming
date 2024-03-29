# Задача 31. Роботландия
# Сообщество роботов живет по следующим законам:
# - один раз в начале года они объединяются в группы по три или пять роботов;
# - за год группа из 3 роботов собирает 5 новых,
#        а группа из 5 роботов собирает 9 новых;
# - роботы собираются так, чтобы собрать за год наибольшее количество;
# - каждый робот живет три года после сборки.
# Известно начальное количество роботов К и все они только что собраны.
# Сколько роботов будет через N лет?

k = int(input('Начальное количество роботов...'))
n = int(input('Количество лет...'))
s0 = k
s1 = 0
s2 = 0
s3 = 0

for i in range(n + 1):
    s = s0 + s1 + s2 + s3
    if s % 5 == 0:
        x = (s // 5) * 9
    elif s % 5 == 1:
        if s == 1:
            x = 0
        else:
            x = (((s - 5) // 5) * 9) + 10
    elif s % 5 == 2:
        if s == 2:
            x = 0
        elif s == 7:
            x = 10
        else:
            x = (((s - 10) // 5) * 9) + 20
    elif s % 5 == 3:
        x = ((s // 5) * 9) + 5
    else:
        if s == 4:
            x = 5
        else:
            x = (((s - 5) // 5) * 9) + 15

    s3 = s2
    s2 = s1
    s1 = s0
    s0 = x

print('Через', n, 'лет будет', s, 'роботов')
