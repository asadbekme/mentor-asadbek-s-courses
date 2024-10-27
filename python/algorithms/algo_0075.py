from math import *

n, k = map(int, input().split())
s = 0

for i in range(n + 1):
    s += (pow(-1, i) * pow(k, i)) / factorial(i)

print("%.3f" % s)