import math

def multiply_list(numbers):
    return math.prod(numbers)

n = int(input())
my_list = []
for i in range (1, n+1):
    numbers = int(input())
    my_list.append(numbers)
result = multiply_list(my_list)
print(result)
