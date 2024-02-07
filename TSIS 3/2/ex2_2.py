def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

num_elements = int(input())

original_list = []

for i in range(num_elements):
    value = int(input())
    original_list.append(value)
    
result = unique_elements(original_list)
print("Original List:", original_list)
print("List with Unique Elements:", result)
