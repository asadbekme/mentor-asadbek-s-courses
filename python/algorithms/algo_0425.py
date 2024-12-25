n = int(input())
array = list(map(int, input().split()))

new_array = []
for element in array:
    if element % 2 == 1:
        new_array.append(element)

average_value = sum(new_array) / len(new_array)
print("%.2f" % average_value)