# * 1-st way:
# n = int(input())
# array = list(map(int, input().split()))
# array1 = sorted(array)
# array2 = sorted(array, reverse = True)
# print(*array1)
# print(*array2)

# * 2-nd way:
n = int(input())
array = list(map(int, input().split()))
# * Bubble sort:
# increasing order:
for i in range(n):
    for j in range(n - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(*array)

# decreasing order:
for i in range(n):
    for j in range(n - 1):
        if array[j] < array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(*array)

