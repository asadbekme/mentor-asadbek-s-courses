n = int(input())
array = list(map(int, input().split()))
min_value = min(array)
counter = array.count(min_value)
print(counter)