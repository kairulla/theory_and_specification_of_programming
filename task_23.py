# Задача 23. Выборы
# На избирательном участке в списке из 100 избирателей
# указываются фамилия и название улицы, на которой проживает избиратель.
# Определить, сколько избирателей живет на улице Богуна.

n = 10
class data:
    def __init__(self):
        self.name = ""
        self.street = ""

a = [data() for _ in range(n)]
count = 0

for i in range(n):
    print('Избиратель', i+1)
    print('Имя...')
    a[i].name = input()
    print('Улица...')
    a[i].street = input()
    if a[i].street == 'Богуна':
        print(a[i].name, 'живет на Богуна.')
        count += 1

print('Всего', count, 'избирателей живут на Богуна.')
