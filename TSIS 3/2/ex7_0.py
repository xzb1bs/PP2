def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
num_elements = int(input())
numbers = []
for i in range(num_elements):
    value = int(input())
    numbers.append(value)
result = has_adjacent_3(numbers)
print(result)
