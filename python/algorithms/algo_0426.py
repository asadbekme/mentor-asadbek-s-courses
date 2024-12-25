n = int(input())
array = list(map(int, input().split()))

for index in range(n):
    if array[index] % 2 == 0:
        array[index] = 0

print(*array)