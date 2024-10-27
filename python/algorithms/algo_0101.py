n = int(input())
array = list(map(int, input().split()))
s, summa = 0, 0
l = len(array)
new_array = []

for element in array:
    s += element
average_value = s / l

for i in range(l):
    if array[i] < average_value:
        new_array.append(array[i])
        summa += array[i]

print("%.2f" % (summa / len(new_array)))
