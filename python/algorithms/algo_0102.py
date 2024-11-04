# n = int(input())
# array = list(map(int, input().split()))
# a, b = map(int, input().split())

# min_value = min(array)
# new_array = []

# for i in range(n):
#     if i >= a - 1 and i <= b - 1:
#         new_array.append("%.1f" % (array[i] / min_value))
#     else:
#         new_array.append("%.1f" % array[i])

# print(* new_array)

# * 2-nd way
from math import ceil

n = int(input())
array = list(map(int, input().split()))

a, b = map(int, input().split())
min_value = min(array)
for index in range(len(array)):
    if a - 1 <= index <= b - 1:
        x = array[index] / min_value
        if (x * 100) % 10 == 5:
            x = ceil(x * 10) / 10
        array[index] = x

for item in array:
    print("%.1f" % item, end = " ")