n = int(input())
array = list(map(int, input().split()))
k, l = map(int, input().split())
s = 0
sliced_array = array[k - 1:l]

for element in sliced_array:
    s += element

average_value = s / len(sliced_array)

print("%.1f" % average_value)
