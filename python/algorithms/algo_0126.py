from math import log

n = int(input())
array = list(map(int, input().split()))

average_value = sum(array) / n
new_array = []

for element in array:
    if element < 0:
        new_array.append(log(average_value))
    else:
        new_array.append(element)

for element in new_array:
    print("%.2f" % element, end = " ")
        
