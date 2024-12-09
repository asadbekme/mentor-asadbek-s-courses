n = int(input())
c = int(input())
array = list(map(int, input().split()))

p = 1
for element in array:
    if element < c:
        p *= element

print(p)
