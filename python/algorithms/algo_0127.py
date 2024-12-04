n = int(input())
array = list(map(int, input().split()))

min_value = min(array)

for index in range(n):
    if array[index] < 0:
        array[index] = pow(min_value, 2)

print(*array)