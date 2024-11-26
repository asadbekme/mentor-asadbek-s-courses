# * 1-st way
# n = int(input())
# array = list(map(int, input().split()))

# max_element = max(array)

# for element in array:
#     print("%.2f" % (element / max_element + 0.00001), end = " ")

# * 2-nd way
from math import ceil
n = int(input())
array = list(map(int, input().split()))

highest_element = max(array)

for index in range(n):
    value = array[index] / highest_element
    if (value * 1000) % 10 == 5:
        value = ceil(value * 10 ** 2) / 10 ** 2
    array[index] = value

for element in array:
    print("%.2f" % element, end = " ")


