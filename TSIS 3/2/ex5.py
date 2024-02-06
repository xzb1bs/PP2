from itertools import permutations

def print_permutations():
    input_string = input("Введите строку: ")
    all_permutations = [''.join(perm) for perm in permutations(input_string)]
    
    print("Все перестановки строки:")
    for perm in all_permutations:
        print(perm)

# Пример использования функции
print_permutations()
