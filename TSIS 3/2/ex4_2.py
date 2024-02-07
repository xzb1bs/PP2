def histogram(numbers):
    for num in numbers:
        print('*' * num)

num_elements = int(input())

numbers = []

for i in range(num_elements):
    value = int(input())
    numbers.append(value)

histogram(numbers)
