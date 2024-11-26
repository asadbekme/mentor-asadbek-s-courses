n = int(input())
array = list(map(int, input().split()))
x, y = map(int, input().split())

count = 0
for element in array:
    if not(element >= x and element <= y):
        count += 1

print(count)