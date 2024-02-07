def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
num_elements = int(input())
numbers_list = []
for i in range(num_elements):
    value = int(input())
    numbers_list.append(value)
result = filter_prime(numbers_list)
print("Ориг:", numbers_list)
print("Простые числа орига:", result)
