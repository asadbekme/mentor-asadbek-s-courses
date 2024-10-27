n = int(input())
array = list(map(int, input().split()))
a, b = map(int, input().split())
s = 0
l = 0

for i in range(n):
    if not(i >= a - 1 and i <= b - 1):
        l += 1
        s += array[i]

print("%.2f" % (s / l))


