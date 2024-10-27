n = int(input())
array = list(map(int, input().split()))
k, m = map(int, input().split())
p = 1

for element in array:
    if element == m:
        p *= element
    if element == k:
        p *= element

print(p)