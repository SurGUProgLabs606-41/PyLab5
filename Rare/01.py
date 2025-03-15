def apply_function_n_times(func, n, value):
    for _ in range(n):
        value = func(value)
    return value

def significant_change_generator(sequence, func, n, threshold=1):
    for item in sequence:
        new_item = apply_function_n_times(func, n, item)
        if abs(new_item - item) >= threshold:
            yield new_item

# Пример использования:

# Функция, которую будем применять
def square(x):
    return x ** 2

# Последовательность чисел
sequence = [1, 2, 3, 4, 5]

# Применяем функцию square к каждому элементу последовательности 2 раза
n = 2
threshold = 10  # Порог значительного изменения

# Фильтруем элементы, которые изменились значительно
result = list(significant_change_generator(sequence, square, n, threshold))

print(result)