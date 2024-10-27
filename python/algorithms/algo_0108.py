n = int(input())
array = list(map(int, input().split()))

min_value = min(array)

for element in array:
    print("%.2f" % (element / min_value), end = " ")