def solve(numheads, numlegs):
    # Условия, учитывающие только целочисленные значения кур и кроликов
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if 2 * num_chickens + 4 * num_rabbits == numlegs:
            return num_chickens, num_rabbits
    # Если нет решения, возвращаем None
    return None

# Пример использования функции
num_heads = 35
num_legs = 94
result = solve(num_heads, num_legs)

if result:
    chickens, rabbits = result
    print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")
else:
    print("Нет решения для заданных параметров.")
