import random
#Создание матрицы произвольного размера от 4 до 8
rows = random.randint(4, 8)
cols = random.randint(4, 8)
#Список значений для заполнения матрицы
values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]
#Создание и заполнение матрицы случайными значениями из списка
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.choice(values))
    matrix.append(row)
#Вывод матрицы в форматированном виде
print("Матрица:")
for i in range(rows):
    for j in range(cols):
        print(f"{matrix[i][j]:4}", end=" ")
    print()
#Вычисление сумму всех нечетных элементов
odd_sum = 0
for i in range(rows):
    for j in range(cols):
#Проверка, нечетное ли число
        if matrix[i][j] % 2 != 0:  
            odd_sum += matrix[i][j]
print(f"\nСумма всех нечетных элементов: {odd_sum}")
