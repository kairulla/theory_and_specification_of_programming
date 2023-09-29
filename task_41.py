# Задача 41.
# Написать программу читающую фразу наоборот и удаляющую букву «а».

# Введите фразу
phrase = input("Введите фразу: ")

# Читаем фразу наоборот
reversed_phrase = phrase[::-1]

# Удаляем букву 'а' (и 'А') из фразы
filtered_phrase = ''.join(char for char in reversed_phrase if char.lower() != 'а')

# Выводим результат
print("Фраза наоборот и без буквы 'а':", filtered_phrase)
