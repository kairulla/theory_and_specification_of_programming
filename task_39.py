# Задача 39.
# Написать программу,
# которая выводит на экран сообщение в телеграфном стиле,
# т.е. буквы сообщения должны появляться по одной,
# причем с некоторой задержкой.

import time

def telegram_style_message(message, delay=0.5):
    for char in message:
        print(char, end='', flush=True)  # Печатаем символ без перевода строки и сразу выводим на экран
        time.sleep(delay)  # Добавляем задержку между символами

# Введите ваше сообщение здесь
message = "Привет, мир!"

# Вызов функции с задержкой 0.5 секунды между символами
telegram_style_message(message, 0.5)

# Добавьте перевод строки в конце для корректного вывода следующего текста
print()
