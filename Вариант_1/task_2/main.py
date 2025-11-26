#Вариант 2
import random
def create_matrix():
    # Заданный список значений
    values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]
    # Генерируем случайный размер матрицы от 4 до 8
    size = random.randint(4, 8)
    # Создаем матрицу, заполняя ее значениями из списка
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            # Используем значения из списка по кругу
            row.append(values[(i * size + j) % len(values)])
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    # Выводим матрицу в форматированном виде
    for row in matrix:
        # Форматируем каждое число с выравниванием
        formatted_row = [f"{num:3}" for num in row]
        print(" ".join(formatted_row))
def sum_odd_numbers(matrix):
    # Вычисляем сумму нечетных чисел в матрице
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:  # Проверяем, что число нечетное
                total += num
    return total
# Основная программа
matrix = create_matrix()
print("Сгенерированная матрица:")
print_matrix(matrix)
# Вычисляем и выводим сумму нечетных чисел
odd_sum = sum_odd_numbers(matrix)
print(f"\nСумма нечетных чисел в матрице: {odd_sum}")
