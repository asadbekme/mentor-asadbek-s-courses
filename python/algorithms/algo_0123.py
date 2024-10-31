n = int(input())
array = list(map(int, input().split()))
s = 0

for index in range(n):
    if (index + 1) % 2 == 0:
        s += array[index]

for element in array:
    if element % 2 == 1 and element > 0:
        print("%.2f" % (element / s), end=" ")
    else:
        print("%.2f" % element, end=" ")
