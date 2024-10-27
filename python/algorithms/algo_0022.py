import math as m

x1, x2, c, d = map(eval, input().split())

a = m.fabs(c * m.pow(x2, 3) + d * m.pow(x1, 3) - c * d)
b = m.sqrt((c * m.pow(x1, 2) + d * m.pow(x2, 2) + 5) + 2)
g = m.tan(x1 * m.pow(x2, 2) + m.pow(d, 3))
f = m.fabs(m.pow(m.sin(a), 2) / b) + g
print("%.2f" % f)