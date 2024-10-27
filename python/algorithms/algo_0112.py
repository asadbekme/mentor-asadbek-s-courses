n = int(input())
array = list(map(int, input().split()))
s, p = 0, 1

for i in range(n):
    if i % 2 == 0:
        p *= array[i]
    else:
        s += array[i]

print("%.2f" % (p / s))