# Импорт модулей
from pathlib import Path
from datetime import datetime
import json

# Создание папки и файла
data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

file_path = data_dir / "notes.json"


# --- Загрузка данных ---
def load_notes():
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# --- Сохранение данных ---
def save_notes(notes):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)


# --- Добавление заметки ---
def add_note():
    print("\n--- Новая заметка ---")

    title = input("Введите заголовок: ")
    text = input("Введите текст: ")

    # Текущая дата и время
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y %H:%M")

    note = {
        "title": title,
        "text": text,
        "date": date_str
    }

    notes = load_notes()
    notes.append(note)
    save_notes(notes)

    print("Заметка сохранена!")


# --- Показ всех заметок ---
def show_notes():
    print("\n--- Все заметки ---")

    notes = load_notes()

    if not notes:
        print("Нет заметок.")
        return

    for i, note in enumerate(notes, 1):
        print(f"\nЗаметка {i}")
        print(f"Дата: {note['date']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['text']}")

    print(f"\nВсего заметок: {len(notes)}")


# --- Поиск по дате ---
def find_by_date():
    print("\n--- Поиск по дате ---")

    search_date = input("Введите дату (ДД.ММ.ГГГГ): ")

    notes = load_notes()
    found = False

    for note in notes:
        if note["date"].startswith(search_date):
            print("\nНайдена заметка:")
            print(f"Дата: {note['date']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['text']}")
            found = True

    if not found:
        print("Заметки за эту дату не найдены.")


# --- Главное меню ---
def main():
    while True:
        print("\n" + "=" * 40)
        print("        ДНЕВНИК ЗАМЕТОК")
        print("=" * 40)

        print("\n1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Найти по дате")
        print("4. Выход")

        choice = input("\nВаш выбор: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            find_by_date()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный выбор!")


# Запуск
main()