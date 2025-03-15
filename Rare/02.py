from functools import reduce


def apply_function_n_times(func, n, value):
    return reduce(lambda acc, _: func(acc), range(n), value)


def significant_change_generator(sequence, func, n, threshold=1):
    # Применяем функцию func к каждому элементу n раз с помощью map
    transformed_sequence = map(lambda x: apply_function_n_times(func, n, x), sequence)

    # Фильтруем элементы, которые изменились значительно с помощью filter
    filtered_sequence = filter(lambda x: abs(x[1] - x[0]) >= threshold, zip(sequence, transformed_sequence))

    # Возвращаем только измененные элементы
    for original, transformed in filtered_sequence:
        yield transformed


# Пример использования:

# Функция, которую будем применять
def square(x):
    return x ** 2


# Последовательность чисел
sequence = [1, 2, 3, 4, 5]

# Применяем функцию square к каждому элементу последовательности 2 раза
n = 2
threshold = 10  # Порог значительного изменения

# Получаем результат
result = list(significant_change_generator(sequence, square, n, threshold))

print(result)