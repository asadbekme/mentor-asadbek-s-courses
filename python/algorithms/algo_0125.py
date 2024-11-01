n = int(input())
a = list(map(int, input().split()))
k, l = map(int, input().split())

sliced_a = a[k - 1:l]
s = 0
for element in sliced_a:
    s += pow(element, 3)
print(s)
