"""
Консольный калькулятор — точка входа.

Меню, ввод значений и диспетчер операций. Кто добавляет новую операцию
в operations.py, дописывает сюда:
  1) импорт функции
  2) пункт в print_menu()
  3) запись в словарь one_arg_ops / two_arg_ops внутри dispatch()
"""

from operations import (
    add, subtract, multiply, divide, modulo,
    sin_deg, cos_deg, power, square_root, floor_value, ceil_value,
)
from memory import Memory


def print_menu():
    print("\n--- Калькулятор ---")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Остаток от деления")
    print("6. Sin")
    print("7. Cos")
    print("8. Возведение в степень")
    print("9. Квадратный корень")
    print("10. Округление вниз (floor)")
    print("11. Округление вверх (ceil)")
    print("12. Память: M+")
    print("13. Память: M-")
    print("14. Память: MR (показать)")
    print("15. Память: MC (очистить)")
    print("16. Память: MS (записать)")
    print("0. Выход")


def read_number(prompt="Введите число: "):
    """Спрашивает число, пока пользователь не введёт корректное."""
    while True:
        raw = input(prompt).replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите корректное число.")


def dispatch(choice, memory):
    # операции с двумя аргументами
    two_arg_ops = {
        "1": ("Сложение", add),
        "2": ("Вычитание", subtract),
        "3": ("Умножение", multiply),
        "4": ("Деление", divide),
        "5": ("Остаток от деления", modulo),
        "8": ("Возведение в степень", power),
    }

    # операции с одним аргументом
    one_arg_ops = {
        "6": ("Sin", sin_deg),
        "7": ("Cos", cos_deg),
        "9": ("Квадратный корень", square_root),
        "10": ("Округление вниз", floor_value),
        "11": ("Округление вверх", ceil_value),
    }

    if choice in two_arg_ops:
        name, func = two_arg_ops[choice]
        a = read_number("Первое число: ")
        b = read_number("Второе число: ")
        try:
            print(f"{name}: {func(a, b)}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Ошибка: {e}")

    elif choice in one_arg_ops:
        name, func = one_arg_ops[choice]
        x = read_number("Число: ")
        try:
            print(f"{name}: {func(x)}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    elif choice == "12":
        memory.madd(read_number("Число для M+: "))
        print(f"Память: {memory.mrecall()}")

    elif choice == "13":
        memory.msubtract(read_number("Число для M-: "))
        print(f"Память: {memory.mrecall()}")

    elif choice == "14":
        print(f"Память (MR): {memory.mrecall()}")

    elif choice == "15":
        memory.mclear()
        print("Память очищена (MC)")

    elif choice == "16":
        memory.mstore(read_number("Число для записи в память (MS): "))
        print(f"Память записана: {memory.mrecall()}")

    else:
        print("Неизвестная команда.")


def main():
    memory = Memory()
    while True:
        print_menu()
        choice = input("Выберите операцию: ").strip()
        if choice == "0":
            print("Выход.")
            break
        dispatch(choice, memory)


if __name__ == "__main__":
    main()