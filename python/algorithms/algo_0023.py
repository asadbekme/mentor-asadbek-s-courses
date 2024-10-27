import math as m

a, b, c, d, x = map(eval, input().split())
try:
    e = a * m.pow(x, 2) + b * x + c
    f = x * m.pow(a, 3) + m.pow(a, 2) + m.pow(a, b - c)
    g = m.fabs((a * x + b) / (c * x + d + m.pow(2, c)))
    y = e / f + m.cos(g)
    print("%.2f" % y)
except:
    print("1.00")
