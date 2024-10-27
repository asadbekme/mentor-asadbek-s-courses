import math as m

x, y = map(float, input().split())
a = 2 * m.tan(x + m.pi / 6)
b = 1 / 3 + m.pow(m.cos(y + x * x), 2)
c = m.log2(x * x + 2)
f1 = a / b + c
print("%.2f" % f1)