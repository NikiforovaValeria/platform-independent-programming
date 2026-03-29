# Импортируем модуль для получения текущего года
from datetime import datetime

# Получаем текущий год
current_year = datetime.now().year

# Вывод заголовка
print("*" * 40)
print("*{:^38}*".format("Личная визитка"))
print("*" * 40)

# Ввод данных пользователя
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")

# Преобразование в целое число
birth_year = int(input("Введите год рождения: "))

# Преобразование в число с плавающей точкой
height = float(input("Введите ваш рост (см): "))

# Вычисление возраста
age = current_year - birth_year

# Вывод результата
print("\n" + "*" * 40)
print("*{:^38}*".format("ВАША ВИЗИТКА"))
print("*" * 40)

# Форматированный вывод данных
print("* {:<36}*".format(f"Имя: {name}"))
print("* {:<36}*".format(f"Фамилия: {surname}"))
print("* {:<36}*".format(f"Год рождения: {birth_year}"))
print("* {:<36}*".format(f"Возраст: {age} лет"))
print("* {:<36}*".format(f"Рост: {height} см"))

print("*" * 40)