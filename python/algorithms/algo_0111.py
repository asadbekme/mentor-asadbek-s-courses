n = int(input())
array = list(map(int, input().split()))
m = int(input())

sum = 0
for element in array:
    if element > m:
        sum += element

print(sum)