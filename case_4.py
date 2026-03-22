import random
import json
import os

# ---------------------- Конфигурация игры ----------------------
# Параметры по умолчанию (можно изменять без изменения кода)
DEFAULT_MIN = 1
DEFAULT_MAX = 100
DEFAULT_ATTEMPTS = 7

# Файл для сохранения статистики
STATS_FILE = "guess_stats.json"

# ---------------------- Статистика ----------------------------
def load_stats():
    """Загружает статистику из файла (если есть) или возвращает пустой словарь."""
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"games": 0, "wins": 0, "total_attempts": 0}
    else:
        return {"games": 0, "wins": 0, "total_attempts": 0}

def save_stats(stats):
    """Сохраняет статистику в файл."""
    try:
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4)
    except IOError:
        print("Не удалось сохранить статистику.")

def update_stats(won, attempts_used):
    """Обновляет статистику после каждой игры."""
    stats = load_stats()
    stats["games"] += 1
    if won:
        stats["wins"] += 1
    stats["total_attempts"] += attempts_used
    save_stats(stats)
    return stats

# ---------------------- Игровая логика -------------------------
def play_game(min_num, max_num, max_attempts):
    """
    Проводит одну игру: загадывает число, принимает попытки,
    возвращает (победа, количество использованных попыток).
    """
    secret = random.randint(min_num, max_num)
    attempts = 0

    print(f"\n🎲 Я загадал число от {min_num} до {max_num}. У тебя {max_attempts} попыток.")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess_input = input(f"Попытка {attempts + 1} (осталось {remaining}): ")
            guess = int(guess_input)
            if not (min_num <= guess <= max_num):
                print(f"❌ Число должно быть в диапазоне от {min_num} до {max_num}.")
                continue
        except ValueError:
            print("❌ Пожалуйста, введите целое число.")
            continue

        attempts += 1

        if guess < secret:
            print("📉 Слишком маленькое!")
        elif guess > secret:
            print("📈 Слишком большое!")
        else:
            print(f"🎉 Поздравляю! Ты угадал число {secret} с {attempts} попытки(ок)!")
            return True, attempts

    print(f"😞 Попытки закончились. Загаданное число было {secret}.")
    return False, attempts

# ---------------------- Главный цикл ---------------------------
def main():
    # Загрузка статистики
    stats = load_stats()
    print("Добро пожаловать в игру «Угадай число»!")
    print("Инструкция:")
    print("  - Компьютер загадывает случайное число в заданном диапазоне.")
    print("  - Твоя задача – угадать его за ограниченное количество попыток.")
    print("  - После каждой попытки ты получишь подсказку: «Слишком маленькое» или «Слишком большое».")
    print("  - Если попытки закончатся, игра покажет правильный ответ.")
    print("  - В конце игры ты можешь начать заново или выйти.")
    print()

    # Параметры текущей игры (можно изменять, не переписывая код)
    min_num = DEFAULT_MIN
    max_num = DEFAULT_MAX
    max_attempts = DEFAULT_ATTEMPTS

    # Демонстрация возможности расширяемости
    print(f"Текущие настройки: диапазон [{min_num}, {max_num}], попыток: {max_attempts}")
    choice = input("Хочешь изменить настройки? (y/n): ").strip().lower()
    if choice == 'y':
        try:
            new_min = int(input(f"Введите минимальное число (по умолчанию {DEFAULT_MIN}): ") or DEFAULT_MIN)
            new_max = int(input(f"Введите максимальное число (по умолчанию {DEFAULT_MAX}): ") or DEFAULT_MAX)
            new_attempts = int(input(f"Введите количество попыток (по умолчанию {DEFAULT_ATTEMPTS}): ") or DEFAULT_ATTEMPTS)
            if new_min < new_max and new_attempts > 0:
                min_num, max_num, max_attempts = new_min, new_max, new_attempts
            else:
                print("Некорректные настройки. Использую значения по умолчанию.")
        except ValueError:
            print("Ошибка ввода. Использую значения по умолчанию.")

    while True:
        won, attempts_used = play_game(min_num, max_num, max_attempts)

        # Обновление статистики
        stats = update_stats(won, attempts_used)
        print("\n📊 Статистика:")
        print(f"  Сыграно игр: {stats['games']}")
        print(f"  Побед: {stats['wins']} ({stats['wins']/stats['games']*100:.1f}%)" if stats['games']>0 else "  Побед: 0")
        avg_attempts = stats['total_attempts'] / stats['games'] if stats['games'] > 0 else 0
        print(f"  Среднее количество попыток: {avg_attempts:.1f}")

        again = input("\nСыграть ещё раз? (y/n): ").strip().lower()
        if again != 'y':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
