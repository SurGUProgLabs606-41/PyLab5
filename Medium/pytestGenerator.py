import pytest
from functools import reduce

# Импортируем функции, которые будем тестировать
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

# Тесты для функции apply_function_n_times
def test_apply_function_n_times():
    # Тест 1: Применение функции square 2 раза к числу 2
    def square(x):
        return x ** 2

    assert apply_function_n_times(square, 2, 2) == 16  # (2^2)^2 = 16

    # Тест 2: Применение функции increment 3 раза к числу 1
    def increment(x):
        return x + 1

    assert apply_function_n_times(increment, 3, 1) == 4  # 1 + 1 + 1 + 1 = 4

    # Тест 3: Применение функции identity 0 раз (ничего не должно измениться)
    def identity(x):
        return x

    assert apply_function_n_times(identity, 0, 5) == 5

# Тесты для функции significant_change_generator
def test_significant_change_generator():
    # Тест 1: Проверка значительного изменения с функцией square и порогом 10
    def square(x):
        return x ** 2

    sequence = [1, 2, 3, 4, 5]
    n = 2
    threshold = 10

    result = list(significant_change_generator(sequence, square, n, threshold))
    assert result == [16, 81, 256, 625]  # Исправленный ожидаемый результат

# Запуск тестов
if __name__ == "__main__":
    pytest.main()