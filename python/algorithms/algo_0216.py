from math import *
a, b, c, x, y = map(float, input().split())
d = pow(x, 1 / 6) + sqrt(pow(a, 2) + pow(b, 2))
e = log(y, x) / pow(c, 3)
f = fabs(sin(x) + cos(y))
g = d + e - f + 2 / 5
print("%.3f" % g)