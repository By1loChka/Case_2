import math
def factorial(n: int) -> int:
    return math.factorial(n)
while True:
    user_input = input("Введите положительное целое число: ")
    try:
        number = int(user_input)
        if number < 0:
            print("Ошибка: число должно быть положительным (или 0).")
            continue
        result = factorial(number)
        print(f"Факториал числа {number} равен {result}")
        break
    except ValueError:
        print("Ошибка: введите целое число.")
