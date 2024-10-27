import math as m

x, y = map(float, input().split())

a = m.pow(x + y, 2) + m.sqrt(m.fabs(y) + 2)
b = x - (x * y) / (m.pow(x, 2) / 2 - 5)
c = m.pow(m.cos(x + y), 2) / m.pow(x + y, 1 / 3)
z = m.log(m.fabs(a - b)) + c

print("%.2f" % z)