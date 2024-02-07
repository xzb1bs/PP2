from itertools import permutations

def print_permutations():
    string = input("Введите строку: ")
    all_permutations = [''.join(perm) for perm in permutations(string)]
    
    print("Все перестановки строки:")
    for perm in all_permutations:
        print(perm)

print_permutations()
