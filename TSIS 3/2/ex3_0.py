def solve(numheads, numlegs):
    
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if 2 * num_chickens + 4 * num_rabbits == numlegs:
            return num_chickens, num_rabbits
    return 0


num_heads = int(input())
num_legs = int(input())
result = solve(num_heads, num_legs)

if result:
    chickens, rabbits = result
    print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")
else:
    print("Нет решения для заданных параметров.")
