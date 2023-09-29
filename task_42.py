# Задача 42. Подсчитать количество удаленных букв «а».

# Введите фразу
phrase = input("Введите фразу: ")

# Читаем фразу наоборот
reversed_phrase = phrase[::-1]

# Удаляем букву 'а' (и 'А') из фразы и подсчитываем их количество
deleted_a_count = 0
filtered_phrase = ''
for char in reversed_phrase:
    if char.lower() != 'а':
        filtered_phrase += char
    else:
        deleted_a_count += 1

# Выводим результат
print("Фраза наоборот и без буквы 'а':", filtered_phrase)
print("Количество удаленных букв 'а':", deleted_a_count)
