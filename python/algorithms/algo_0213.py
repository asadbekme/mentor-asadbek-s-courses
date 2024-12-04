# * 1-st way
# n = int(input())
# array = list(map(int, input().split()))

# max_element = max(array)
# count = 0

# for element in array:
#     if element == max_element:
#         count += 1

# print(max_element, count)

# * 2-nd way
n = int(input())
array = list(map(int, input().split()))

max_element = array[0]
for element in array:
    if element > max_element:
        max_element = element
        
count = array.count(max_element)

print(max_element, count)