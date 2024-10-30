n, x = map(int, input().split())

s = 0
for index in range(1, n + 1):
    s += pow(x, 2 * index - 1) / (2 * index - 1)

print("%.3f" % s)
