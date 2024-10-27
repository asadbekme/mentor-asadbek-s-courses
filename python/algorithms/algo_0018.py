import math as m

x, y  = map(float, input().split())

a = 1 / (x + 2 / (x * x) + 3 / m.pow(x, 3))
b = m.exp(x * x + 3 * x)
c = m.atan(x + y) + m.pow(m.fabs(5 + x), 2)
d = m.pow(m.cos(y * y + m.pow(x, 2) / 2), 2)
f = (a + b) / c - d

print("%.2f" % f)