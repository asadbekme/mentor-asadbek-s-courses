from math import pow
x, n = map(int, input().split())

s, i = 0, 1
while i <= n:
    s += pow(x + 1, 1 / i)
    i += 1
print("%.2f" % s)