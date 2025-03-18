from functools import reduce

# Функция, которая применяет функцию func к значению value n раз
def apply_function_n_times(func, n, value):
    # Используется reduce для последовательного применения функции func
    # lambda acc, _: func(acc) — применяет func к текущему значению acc
    # range(n) — создает последовательность из n элементов (количество применений)
    # value — начальное значение
    return reduce(lambda acc, _: func(acc), range(n), value)

# Генератор, который фильтрует элементы последовательности, оставляя только те, которые изменились значительно после применения функции func n раз
def significant_change_generator(sequence, func, n, threshold=1):
    # Применение функции func к каждому элементу sequence n раз с помощью map
    # lambda x: apply_function_n_times(func, n, x) — применяет func n раз к каждому x
    transformed_sequence = map(lambda x: apply_function_n_times(func, n, x), sequence)

    # Фильтруем элементы, которые изменились значительно с помощью filter
    # zip(sequence, transformed_sequence) — создает пары (original, transformed)
    # lambda x: abs(x[1] - x[0]) >= threshold — проверяет, превышает ли разница порог
    filtered_sequence = filter(lambda x: abs(x[1] - x[0]) >= threshold, zip(sequence, transformed_sequence))

    # Возвращаем только измененные элементы
    for original, transformed in filtered_sequence:
        yield transformed # Возвращаем transformed как часть генератора
        # yield — это ключевое слово в Python, которое используется в функциях для создания генераторов.
        # Генераторы — это специальные итераторы, которые генерируют значения "на лету" (лениво).

# Пример использования:

# Функция, которая будет применяться (возведение числа в квадрат)
def square(x):
    return x ** 2

# Последовательность чисел
sequence = [1, 2, 3, 4, 5]

# Применяем функцию square к каждому элементу последовательности 2 раза
n = 2
threshold = 10  # Порог значительного изменения

result = list(significant_change_generator(sequence, square, n, threshold))

print(result)