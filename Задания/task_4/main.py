#Автор darakulkina138-netizen
# Открываем файл и читаем его содержимое
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
# Разбиваем текст на слова (разделители: пробелы, переносы строк и т.д.)
words = text.split()
# Выводим количество слов
print(f"Количество слов в файле: {len(words)}")
