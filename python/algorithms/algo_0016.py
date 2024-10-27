import math as m

x, y = map(float, input().split())
a = (y * y + 2) / (x + m.pow(x, 3) / 5)
c1 = (x + y) / (y * y + m.fabs(a)) + m.exp(y + 2)
print("%.2f" % c1)