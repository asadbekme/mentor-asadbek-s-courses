n = int(input())
array = list(map(int, input().split()))

max_value = max(array)
min_value = min(array)
new_array = []
for element in array:
    if element > 0:
        new_array.append(element * min_value)
    else:
        new_array.append(element * max_value)

print(*new_array)