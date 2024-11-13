from math import log, pow
n, x, y = map(int, input().split())

s, i = 0, 1
while i <= n:
    s += log(pow(y, 2 * i - 1), x) / pow(2, i)
    i += 1
print("%.2f" % s)