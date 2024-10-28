from math import *

n, x = map(int, input().split())
sum = 0

for i in range(1, n + 1):
    sum += pow(x, 2 * i - 1) / factorial(2 * i - 1)

print("%.3f" % sum)