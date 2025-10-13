#Вариант 2
import random
#Создание списка случайных целых чисел от -50 до 50 размером 25 элементов
numbers = [random.randint(-50, 50) for _ in range(25)]
print("Сгенерированный список:")
print(numbers)
#Поиск количество положительных, отрицательных и нулевых элементов
positive_count = len([x for x in numbers if x > 0])
negative_count = len([x for x in numbers if x < 0])
zero_count = len([x for x in numbers if x == 0])
#Вычисление процентов
total_count = len(numbers)
positive_percent = (positive_count / total_count) * 100
negative_percent = (negative_count / total_count) * 100
zero_percent = (zero_count / total_count) * 100
#Вывод статистики
print("\nСтатистика:")
print(f"Положительные элементы: {positive_count} ({positive_percent:.1f}%)")
print(f"Отрицательные элементы: {negative_count} ({negative_percent:.1f}%)")
print(f"Нулевые элементы: {zero_count} ({zero_percent:.1f}%)")
#Поиск самого большого и самого маленького значения
max_value = max(numbers)
min_value = min(numbers)
print(f"\nСамое большое значение: {max_value}")
print(f"Самое маленькое значение: {min_value}")
