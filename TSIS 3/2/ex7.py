def has_adjacent_3(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example of using the function
numbers = [1, 2, 3, 4, 3, 5, 6]
result = has_adjacent_3(numbers)
print(result)
