from math import ceil

n = int(input())
array = list(map(int, input().split()))

new_array = []
for element in array:
    if element % 2 == 1:
        new_array.append(element)
average = sum(new_array) / len(new_array)

if (average * 1000) % 10 == 5:
    average = ceil(average * 10 ** 2) / 10 ** 2

print("%.2f" % average)