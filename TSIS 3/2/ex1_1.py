def contains_007(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

num_elements = int(input())

numbers = []

for i in range(num_elements):
    value = int(input())
    numbers.append(value)
result = contains_007(numbers)
print(result)
