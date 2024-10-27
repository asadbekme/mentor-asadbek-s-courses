import math as m

x, y, z = map(eval, input().split())
a = m.pow(m.fabs(y) + 2, 1 / 4)
b = m.pow(m.exp(x - 1) / m.sin(z + 2) + 2, 1 / 3)
c = m.pow(2, -x) * m.sqrt(x + a)
d = c * b
print("%.2f" % d)