# Задача 4 Поиск палиндромов
# Символьная строка содержит последовательность слов, разделенных пробелами.
# Найти все палиндромы - слова, которые читаются
# слева направо так же,
# как и справа налево.

def Palyndrom(buf):
    ok = True
    i = 0
    k = len(buf)
    while ok and (i < k):
        ok = (buf[i] == buf[k-1])
        i += 1
        k -= 1
    return ok

s = input('Введите исходную строку...')
i = 0
while i < len(s):
    while s[i] == ' ':
        i += 1
    buf = ''
    while (s[i] != ' ') and (i < len(s)):
        buf += s[i]
        i += 1
    if Palyndrom(buf):
        print(buf, '- палиндром.')