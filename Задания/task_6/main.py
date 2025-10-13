#Вариант 2
import random
import itertools
#Создание случайного списка из 20 значений по 4 случайных целых чисел от -10 до 10
random_list = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)]
print("Сгенерированный список кортежей:")
for i, item in enumerate(random_list, 1):
    print(f"{i}: {item}")
#Поиск всех уникальных значений из всех кортежей
all_values = set()
for tuple_item in random_list:
    all_values.update(tuple_item)
print(f"\nВсе уникальные значения: {sorted(all_values)}")
#Поиск всех уникальных комбинаций из 2 элементов 
unique_combinations = list(itertools.combinations(all_values, 2))
print(f"\nВсе уникальные комбинации из 2 элементов (всего {len(unique_combinations)}):")
#Вывод комбинации с форматированием 
for i in range(0, len(unique_combinations), 5):
    print(unique_combinations[i:i+5])
while True:
    try:
        user_number = int(input("\nВведите целое число: "))
        break
    except ValueError:
        print("Ошибка: введите целое число.")
#Вычисление количество пар, чья сумма меньше заданного пользователем значения
count_pairs = 0
pairs_list = []
for a, b in unique_combinations:
    if a + b < user_number:
        count_pairs += 1
        pairs_list.append((a, b))
#Вывод результата
print(f"\nКоличество пар, чья сумма меньше {user_number}: {count_pairs}")
if pairs_list:
    print("Эти пары:")
    for i in range(0, len(pairs_list), 5):
        print(pairs_list[i:i+5])
else:
    print("Таких пар нет.")
