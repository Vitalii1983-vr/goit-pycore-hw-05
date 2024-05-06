# імпорт модуля sys для роботи (взаємодії) з системними параметрами та функціями
import sys

# імпорт класу Path з модуля pathlib для роботи з файловою системою (хоча в цьому коді клас Path поки не використовується, у майбутньому, для збереження та завантаження контактів, роботою з директоріями та ін. він може знадобитися)
from pathlib import Path

# Декоратор для обробки помилок, які можуть виникнути під час виконання команд.
# Перехоплює специфічні типи винятків і повертає відповідні повідомлення.


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            # Недостатньо аргументів для виконання команди
            return "Give me name and phone please."
        except ValueError:
            return "Enter correct data types."       # Введено некоректні типи даних
        except KeyError:
            return "Enter user name."                # Користувач не знайдений
    return inner


def parse_input(user_input):
    """
    Розбиває рядок вводу користувача на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт у словник контактів. Вимагає два аргументи: ім'я та номер телефону.
    """
    if len(args) != 2:
        raise IndexError("Некоректна кількість аргументів.")
    name, phone = args
    if not phone.isdigit():  # Додаємо перевірку, що номер телефону повинен містити тільки цифри
        raise ValueError("Phone number must contain only digits.")
    contacts[name] = phone
    return "Контакт додано."


@input_error
def change_contact(args, contacts):
    """
    Оновлює інформацію про існуючий контакт. Вимагає два аргументи: ім'я та новий номер телефону.
    """
    if len(args) != 2:
        raise IndexError("Некоректна кількість аргументів.")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"Контакт '{name}' не знайдено.")
    contacts[name] = phone
    return "Контакт оновлено."


@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону за вказаним іменем. Вимагає один аргумент: ім'я.
    """
    if len(args) != 1:
        raise IndexError("Некоректна кількість аргументів.")
    name = args[0]
    if name not in contacts:
        raise KeyError(f"Контакт '{name}' не знайдено.")
    return contacts[name]


@input_error
def show_all(contacts):
    """
    Виводить всі контакти. Якщо контактів немає, повідомляє про це.
    """
    if not contacts:
        return "Контакти не знайдено."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    """
    Головна функція, яка керує потоком команд від користувача.
    """
    contacts = {}
    print("Вітаємо у вашому асистенті боті!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Некоректна команда.")


if __name__ == "__main__":
    main()


# Список команд, які може виконувати бот:
# 1. hello - Бот вітає користувача та запитує, як може допомогти.
# 2. add[ім'я] [телефон] - Додає новий контакт з ім'ям та телефонним номером до списку контактів.
# 3. change[ім'я] [новий телефон] - Змінює телефонний номер існуючого контакту на новий.
# 4. phone [ім'я] - Показує телефонний номер контакту з вказаним ім'ям.
# 5 all - Відображає всі контакти, що зберігаються в боті.
# 6. close або exit - Закриває програму та виводить прощальне повідомлення.
