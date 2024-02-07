def solve(numheads, numlegs):
    
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return 0

heads = int(input())
legs = int(input())
result = solve(heads, legs)

if result:
    chickens, rabbits = result
    print(f"Количество кур: {chickens}, Количество кроликов: {rabbits}")
else:
    print("Нет решения для заданных параметров.")
