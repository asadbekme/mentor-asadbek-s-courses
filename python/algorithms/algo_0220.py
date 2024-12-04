# * 1-st way
# n = int(input())
# array = list(map(int, input().split()))

# max_element = max(array)
# min_element = min(array)
# new_array = []

# for element in array:
#     if element == max_element:
#         new_array.append(min_element)
#     elif element == min_element:
#         new_array.append(max_element)
#     else:
#         new_array.append(element)

# print(*new_array)

# * 2-nd way
n = int(input())
array = list(map(int, input().split()))

max_element = max(array)
min_element = min(array)

for i in range(n):
    if array[i] == max_element:
        array[i] = min_element
    elif array[i] == min_element:
        array[i] = max_element

print(*array)