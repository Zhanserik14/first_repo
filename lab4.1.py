#Напишите программу, используя 10 функциии методы, связанные состроками
# Program using 10 string methods in Python

string = "Hello, World!"

# Пример: 1. Длина строки
print(len(string))

# Пример: 2. Верхний регистр
print(string.upper())

# Пример: 3. Нижний регистр
print(string.lower())

# Пример: 4. Замена подстроки
print(string.replace("World", "Python"))

# Пример: 5. Извлечение подстроки
print(string[7:])

# Пример: 6. Разбиение строки на список по разделителю
print(string.split())

# Пример: 7. Проверка начала строки
print(string.startswith("Hello"))

# Пример: 8. Проверка окончания строки
print(string.endswith("World!"))

# Пример: 9. Удаление пробельных символов в начале и конце строки
print(string.strip())

# Пример: 10. Объединение строк из списка в одну строку с разделителем
list_of_strings = ["Hello", "Python", "World"]
print("-".join(list_of_strings))