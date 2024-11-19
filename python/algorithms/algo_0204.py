n = int(input())
array = list(map(int, input().split()))
m = int(input())

i, new_array = 1, []
while i <= m:
    l, r = map(int, input().split())
    new_array.append(sum(array[l - 1:r]))
    i += 1

if m > 0:
    for element in new_array:
        print(element)