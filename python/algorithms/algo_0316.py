from math import *
n = int(input())

s, i = 0, 1
while i <= n:
    s += cos(i) / i
    i += 1

print("%.2f" % s)
