n = int(input())
array = list(map(int, input().split()))
s = 0

for element in array:
    s += element ** 2

print(s)