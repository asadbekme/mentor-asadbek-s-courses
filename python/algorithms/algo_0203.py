n = int(int(input()))
array = list(map(int, input().split()))
m = int(input())

i, new_array = 1, []
while i <= m:
    l, r, p = map(int, input().split())
    pp = 1
    for j in range(l - 1, r):
        pp *= array[j]
    new_array.append(pp % p)
    i += 1

for element in new_array:
    print(element)