# * 1-st way:
# n = int(input())
# array = list(map(int, input().split()))

# sorted_array = sorted(array, key=lambda x: (abs(x), x))
# print(*sorted_array)

# * 2-nd way:
n = int(input())
array = list(map(int, input().split()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if abs(array[j]) < abs(array[min_index]):
            min_index = j
        elif abs(array[j]) == abs(array[min_index]) and array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(*array)