n = int(input())
array = list(map(int, input().split()))

max_element = max(array)

for element in array:
    print("%.2f" % (element / max_element + 0.00001), end = " ")