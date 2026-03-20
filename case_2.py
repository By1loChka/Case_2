import math

def calculate_factorial(n: int) -> int:
    """Вычисляет факториал числа n с помощью math.factorial."""
    return math.factorial(n)

def get_valid_number() -> int:
    """Запрашивает у пользователя число и валидирует ввод."""
    while True:
        user_input = input("Введите положительное целое число (или 'quit' для выхода): ").strip()

        if user_input.lower() == 'quit':
            return None

        if not user_input:
            print("Ошибка: ввод не должен быть пустым. Попробуйте снова.")
            continue

        try:
            number = int(user_input)
            if number < 0:
                print("Ошибка: число должно быть положительным (или 0). Попробуйте снова.")
                continue
            if number > 1000:
                print("Предупреждение: числа > 1000 могут вызвать проблемы с памятью. Продолжаете? (y/n)")
                if input().lower() != 'y':
                    continue
            return number
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")

def main():
    print("Калькулятор факториалов. Введите 'quit' для выхода.")

    while True:
        number = get_valid_number()
        if number is None:  # пользователь хочет выйти
            print("До свидания!")
            break

        result = calculate_factorial(number)
        print(f"Факториал числа {number} равен {result:,}")  # форматирование с запятыми

if __name__ == "__main__":
    main()
