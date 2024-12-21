n = int(input())
array = list(map(int, input().split()))

positive_count = 0
negative_count = 0

for element in array:
    if element > 0:
        positive_count += 1
    else:
        negative_count += 1

print(positive_count * negative_count)