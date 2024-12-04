n, m = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

merged_array = array1 + array2
merged_array.sort()

for element in merged_array:
    print(element, end = " ")