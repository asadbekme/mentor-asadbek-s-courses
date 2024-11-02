n = int(input())
array = list(map(int, input().split()))

s, count = 0, 0
for element in array:
    if element % 2 == 0:
        s += element
        count += 1

print("%.2f" % (s / count))