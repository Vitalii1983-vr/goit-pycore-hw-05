import os  # Імпорт модуля os для взаємодії з операційною системою
import sys  # Імпорт модуля sys для доступу до деяких змінних, використаних або підтримуваних інтерпретатором


def parse_log_line(line):
    """
    Парсинг одного рядка логу і повернення словника з його компонентами.
    """
    parts = line.split(maxsplit=3)  # Розділяємо рядок на чотири частини
    return {
        'date': parts[0],  # Перша частина - дата
        'time': parts[1],  # Друга частина - час
        'level': parts[2],  # Третя частина - рівень логування
        # Четверта частина - повідомлення, якщо воно існує
        'message': parts[3] if len(parts) > 3 else ''
    }


def load_logs(file_path):
    """
    Завантажує логи з файлу і повертає список записів логів.
    """
    logs = []  # Створення порожнього списку для логів
    with open(file_path, 'r') as file:  # Відкриття файлу для читання
        for line in file:  # Ітерація по кожному рядку у файлі
            # Очищення рядка від пробілів і парсинг
            parsed_line = parse_log_line(line.strip())
            # Додавання розібраного рядка до списку логів
            logs.append(parsed_line)
    return logs  # Повернення списку логів


def filter_logs(logs, filter_func):
    """
    Фільтрація логів за заданою функцією-фільтром.
    """
    return filter(filter_func, logs)


def count_logs_by_level(logs):
    """
    Підрахунок кількості логів для кожного рівня логування.
    """
    counts = {}  # Створення словника для підрахунку
    for log in logs:
        level = log['level']  # Отримання рівня логування
        if level in counts:
            # Інкрементування лічильника, якщо рівень вже існує
            counts[level] += 1
        else:
            # Створення нового запису для рівня, якщо він ще не був зафіксований
            counts[level] = 1
    return counts  # Повернення словника з підрахунками


def display_log_counts(counts):
    """
    Відображення кількості логів за рівнями у вигляді таблиці.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        # Виведення даних у форматованій таблиці
        print(f"{level:15} | {count}")


def main():
    """
    Головна функція, яка керує виконанням скрипту.
    """
    file_path = r"C:\Users\roger\Desktop\Магістратура 2024\My_HW_VR\3_HW_Theme_8\log.txt"  # Шлях до файлу логу

    if not os.path.exists(file_path):
        # Перевірка існування файлу, якщо файлу немає - вивід помилки
        print(f"File not found: {file_path}")
        sys.exit(1)

    # Зчитування рівня логування з аргументів командної строки, якщо вони є
    level_filter = sys.argv[1] if len(sys.argv) > 1 else None

    logs = load_logs(file_path)  # Завантаження логів з файлу
    counts = count_logs_by_level(logs)  # Підрахунок логів за рівнями
    display_log_counts(counts)  # Відображення підрахунків

    if level_filter:
        # Фільтрація логів за заданим рівнем
        filtered_logs = filter_logs(
            logs, lambda log: log['level'] == level_filter.upper())
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        for log in filtered_logs:
            # Виведення детальної інформації про фільтровані логи
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()  # Виконання головної функції, якщо скрипт запущено як головний модуль
