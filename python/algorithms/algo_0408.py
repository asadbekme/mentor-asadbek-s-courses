n = int(input())
array = list(map(int, input().split()))

length = len(array)
left_array = array[:length // 2]
if length % 2 == 0:
    right_array = array[length // 2:]
else:
    right_array = array[length // 2 + 1:]

print(sum(left_array) - sum(right_array))