n = int(input())
array = list(map(int, input().split()))
k, l = map(int, input().split())

# * 1-st way
# s = 0
# sliced_array = array[k - 1 : l]
# for element in sliced_array:
#     s += element
# average_value = s / len(sliced_array)
# print("%.1f" % average_value)

# * 2-nd way
sum, count = 0, 0
for i in range(n):
    if i >= k - 1 and i <= l - 1:
        sum += array[i]
        count += 1
average_value = sum / count
print("%.1f" % average_value)