#Вариант 2
#Запрашиваниие количество строк с проверкой
while True:
    try:
        n = int(input("Введите количество строк: "))
        if n <= 0:
            print("Количество строк должно быть положительным числом.")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое число.")
words_set = set()
#Подсчет строки и разбиваем на слова
for i in range(n):
    line = input(f"Введите строку {i + 1}: ")
#Разбили строку на слова по пробельным символам
    words = line.split()
#Добавление слова в множество
    for word in words:
        words_set.add(word)
#Вывод результата
print(f"Количество различных слов: {len(words_set)}")
