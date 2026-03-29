# Импорт необходимых модулей
from pathlib import Path
from datetime import datetime

# Создание папки data и файла
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "journal.txt"


# --- Проверка корректности даты ---
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# --- Добавление записи ---
def add_entry():
    print("\n--- Добавление новой записи ---")

    # Ввод даты с проверкой
    while True:
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        if validate_date(date):
            break
        print("Ошибка: неверный формат даты!")

    # Ввод текста
    text = input("Введите текст наблюдения: ")

    # Ввод оценки с проверкой
    while True:
        try:
            rating = int(input("Введите оценку (1-10): "))
            if 1 <= rating <= 10:
                break
            else:
                print("Ошибка: оценка должна быть от 1 до 10!")
        except ValueError:
            print("Ошибка: введите число!")

    # Сохранение в файл
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{date} | {rating} | {text}\n")

    print("Запись успешно добавлена!")


# --- Просмотр записей ---
def show_entries():
    print("\n--- Все записи ---")

    if not file_path.exists():
        print("Журнал пуст.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Журнал пуст.")
        return

    print("+------------+--------+--------------------------------+")
    print("|    Дата    | Оценка |            Текст               |")
    print("+------------+--------+--------------------------------+")

    total = 0

    for line in lines:
        date, rating, text = line.strip().split(" | ")
        total += int(rating)
        print(f"| {date:<10} | {rating:^6} | {text:<30} |")

    print("+------------+--------+--------------------------------+")

    count = len(lines)
    avg = total / count

    print("\nСтатистика:")
    print(f"Всего записей: {count}")
    print(f"Средняя оценка: {avg:.2f}")


# --- Очистка журнала ---
def clear_entries():
    open(file_path, "w").close()
    print("Журнал очищен!")


# --- Главное меню ---
def main():
    while True:
        print("\n" + "=" * 40)
        print("       ЖУРНАЛ НАБЛЮДЕНИЙ")
        print("=" * 40)

        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Очистить журнал")
        print("4. Выход")

        choice = input("\nВаш выбор: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            show_entries()
        elif choice == "3":
            clear_entries()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный выбор!")


# Запуск программы
main()