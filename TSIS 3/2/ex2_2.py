def unique_elements(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

num_elements = int(input())
list = []

for i in range(num_elements):
    value = int(input())
    list.append(value)
    
result = unique_elements(list)
print("Original List:", list)
print("List with Unique Elements:", result)
