import math as m

n, x = map(int, input().split())
s = 0

for i in range(1, n + 1):
    s += m.pow(x, i) / m.factorial(i)

print("%.3f" % s)