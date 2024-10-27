import math as m

x = float(input())
y = 2 * m.tan(x + 2) - m.cos(x + m.pow(2, x))
z = 1 + m.pow(m.cos(x + 2), 2)
b = m.sin(x * x) / (m.pow(x, 2) + 3)
a = m.sqrt(y / z) + b
print("%.2f" % a)
